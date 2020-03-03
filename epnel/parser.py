from collections import deque
from sys import stdin

class Lexer():
	def __init__(self, input_file=stdin, string=""):
		if not string:
			string = input_file.read()
		self.data = deque(string.upper().split())

	def next(self):
		if not self.data:
			raise Exception("input empty, lexems missing?")
		return self.data.popleft()

# abstract syntax tree node representation
class AST_Node():
	def __init__(self, value, type="", children=()):
		self.value = value
		self.type = type
		self.children = children

# top-down recursive descent parser
class Parser():
	lexer = None
	ast = None

	def __init__(self, lexer=None, **kwargs):
		if lexer is None:
			self.lexer = Lexer(**kwargs)
		else:
			self.lexer = lexer
		self.ast = self.parse(self.lexer.next())

	def parse(self, token):
		if token in "+-*/<>|^&=":
			return AST_Node(token, "operator", (self.parse(self.lexer.next()), self.parse(self.lexer.next())))
		elif token == "?":
			return AST_Node(token, "conditional", (self.parse(self.lexer.next()), self.parse(self.lexer.next()), self.parse(self.lexer.next())))
		elif token == ".":
			return AST_Node(token, "assignment", (self.parse(self.lexer.next()), self.parse(self.lexer.next())))
		elif token == ",":
			return AST_Node(token, "assignment", (self.parse(self.lexer.next()), self.parse(self.lexer.next()), self.parse(self.lexer.next())))
		elif token == "!":
			return AST_Node(token, "boolean")
		else:
			return AST_Node(token, "number")

	def root(self):
		return self.ast
