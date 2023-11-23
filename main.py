#from src.lexer import lexer
from src.parser_ import parser

f = open("./entrada.txt", "r")
input_text = f.read()
parser.parse(input_text)