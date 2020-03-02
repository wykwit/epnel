symbol_table = dict()

def operator(node):
	if node.value == "+":
		return interpret(node.children[0]) + interpret(node.children[1])
	elif node.value == "-":
		return interpret(node.children[0]) - interpret(node.children[1])
	elif node.value == "*":
		return interpret(node.children[0]) * interpret(node.children[1])
	elif node.value == "/":
		return interpret(node.children[0]) // interpret(node.children[1])
	elif node.value == "<":
		return interpret(node.children[0]) < interpret(node.children[1])
	elif node.value == ">":
		return interpret(node.children[0]) > interpret(node.children[1])
	elif node.value == "|":
		return interpret(node.children[0]) | interpret(node.children[1])
	elif node.value == "^":
		return interpret(node.children[0]) ^ interpret(node.children[1])
	elif node.value == "&":
		return interpret(node.children[0]) & interpret(node.children[1])
	elif node.value == "=":
		return interpret(node.children[0]) == interpret(node.children[1])
	elif node.value == ".":
		symbol_table[node.children[0].value] = interpret(node.children[1])
		return symbol_table[node.children[0].value]
	else:
		raise Exception("invalid operator", node)

def conditional(node):
	if interpret(node.children[0]):
		return interpret(node.children[1])
	else:
		return interpret(node.children[2])

def boolean(node):
	return False

def number(node):
	if node.value in symbol_table:
		return symbol_table[node.value]
	if node.value.isnumeric():
		return int(node.value)
	return 0

def interpret(node):
	if node.type == "operator":
		return operator(node)
	elif node.type == "conditional":
		return conditional(node)
	elif node.type == "boolean":
		return boolean(node)
	elif node.type == "number":
		return number(node)
	else:
		raise Exception("invalid type", node)
