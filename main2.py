
# -----------------------------------------------------------------------------
# Rainman Sián
# 07-02-2020
#
# Ejemplo mi primer proyecto con Python utilizando ply en Ubuntu
# -----------------------------------------------------------------------------

import re

tokens  = (
    'NAV',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'ID',
    'CLICK',
    'URL',
    'ASSIGN',
    'CORIZQ',
    'CORDER',
    'SEMICOLON',
    'TEXT'
)

# Tokens
t_NAV       = r'nav'
t_URL       = r'https?:\/\/[a-zA-Z0-9\-\.\/\?\:@\-_=#]+'
t_ID    = r'//input\[@id="[a-zA-Z0-9_\-]+"\]'
t_ASSIGN    = r'='
t_OPEN_PAREN    = r'\('
t_CLOSE_PAREN    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_SEMICOLON    = r';'
t_CLICK    = r'click'
palabras_clave = ['nav', 'click']
t_TEXT    = fr"(?!({'|'.join(map(re.escape, palabras_clave))}))[a-zA-Z]+"

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Definición de la gramática
def p_instrucciones_lista(t):
    '''commands    : command commands
                   | command '''

def p_command_assignment(p):
    'command : TEXT ASSIGN ID SEMICOLON'
    print('El valor de la expresión es: ' + str(p[3]))

def p_command_nav(p):
    'command : NAV OPEN_PAREN URL CLOSE_PAREN SEMICOLON'
    print('El valor de la expresión es: ' + str(p[3]))

def p_command_click(p):
    'command : CLICK OPEN_PAREN TEXT CLOSE_PAREN SEMICOLON'
    print('El valor de la expresión es: ' + str(p[3]))

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)
