import ply.yacc as yacc
from src.lexer import tokens
from src.commands import *

def p_instrucciones_lista(t):
    '''commands    : command commands
                   | command '''

def p_command_assignment(p):
    'command : TEXT ASSIGN ID PUNTOYCOMA'
    #print('El valor de la expresión es: ' + str(p[3]))

def p_command_nav(p):
    'command : NAV OPEN_PAREN URL CLOSE_PAREN PUNTOYCOMA'
    url = p[3]
    navigate_to_url(url)
    #print('El valor de la expresión es: ' + str(p[3]))

def p_command_click(p):
    'command : CLICK OPEN_PAREN ID CLOSE_PAREN PUNTOYCOMA'
    element_id = p[3]
    click_element(element_id)
    #print('El valor de la expresión es: ' + str(p[3]))

def p_command_text(p):
    'command : TEXT OPEN_PAREN ID COMMA TEXT CLOSE_PAREN PUNTOYCOMA'
    element_id = p[3]
    text = p[5]
    set_text(element_id, text)
    #print('El valor de la expresión es: ' + str(p[3]) + "->" + str(p[5]))

def p_command_get_text(p):
    'command : GET_TEXT OPEN_PAREN ID COMMA TEXT CLOSE_PAREN PUNTOYCOMA'
    element_id = p[3]
    element_text = p[5]
    get_text(element_id, element_text)
    #print('El valor de la expresión es: ' + str(p[3]))

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

# Analizador sintáctico
parser = yacc.yacc()