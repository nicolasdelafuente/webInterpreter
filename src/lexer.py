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
    'ELEMENT_TEXT',
    'ASSERT_TEXT'
)

# Tokens
t_NAV       = r'nav'
t_URL       = r'https?:\/\/[a-zA-Z0-9\-\.\/\?\:@\-_=#]+'
t_ID    = r'//[\w]+\[@[\w]+="[a-zA-Z0-9_\-]+"\][\/\w\[\]]*'
t_ASSIGN    = r'='
t_OPEN_PAREN    = r'\('
t_CLOSE_PAREN    = r'\)'
t_PUNTOYCOMA    = r';'
t_COMMA    = r','
t_CLICK    = r'click'
palabras_clave = ['click', 'elementText', 'nav', 'assertText']
t_TEXT = fr"(?!({'|'.join(map(re.escape, palabras_clave))}))(?!https?://\S+)[\w\s_\-|.\"]+"
t_ELEMENT_TEXT = r'elementText'
t_ASSERT_TEXT = r'assertText'

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
