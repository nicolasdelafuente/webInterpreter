import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens

tokens = [
    'nav',
    '(',
    ')',
    ';',
    '=',
    'text',
    'http://',
    'https://',
    ',',
    'b',
    'click',
    'text',
    'assert',
]
t_nav = r'nav'
t_url = r'https://\S+'
t_nombre = r'[a-zA-Z0-9_-]+'


# Reglas para tokens
t_URL = r'www\.[a-zA-Z0-9]+\.[a-zA-Z]+'
t_SEARCH = r'search'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para manejar errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Reglas de sintaxis
def p_command(p):
    '''command : URL
               | SEARCH'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Error sintáctico en '{p.value}'")
    else:
        print("Error sintáctico al final de la entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()