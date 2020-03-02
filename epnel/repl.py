from .parser import Parser
from .interpreter import interpret

def repl(prompt=":) "):
	while True:
		try:
			_in = input(prompt)
		except:
			break
		p = Parser(string=_in)
		print(interpret(p.root()))

if __name__ == "__main__":
	repl()
