#from src.lexer import lexer
from src.parser_ import parser

f = open("./entrada.txt", "r")
input_text = f.read()
print(input_text)
parser.parse(input_text)