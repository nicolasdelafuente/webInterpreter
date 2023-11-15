import re
import ply.lex as lex

tokens = (
    'NAV',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'ID',
    'CLICK',
    'URL',
    'ASSIGN',
    'PUNTOYCOMA',
    'COMMA',
    'TEXT',
    'GET_TEXT'
)

# Tokens
t_NAV = r'nav'
t_URL = r'https?:\/\/[a-zA-Z0-9\-\.\/\?\:@\-_=#]+'
t_ID = r'//input\[@id="[a-zA-Z0-9_\-]+"\]'
t_ASSIGN = r'='
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_PUNTOYCOMA = r';'
t_COMMA = r','
t_CLICK = r'click'
palabras_clave = ['nav', 'click', 'getText']
t_TEXT = fr"(?!({'|'.join(map(re.escape, palabras_clave))}))[A-Za-z0-9_\- ]+"
t_GET_TEXT = r'getText'

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Analizador léxico
lexer = lex.lex()
