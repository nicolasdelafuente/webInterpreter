import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

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
    'COMMA',
    'TEXT',
    'GET_TEXT'
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
t_COMMA    = r','
t_CLICK    = r'click'
palabras_clave = ['nav', 'click', 'getText']
t_TEXT   = fr"(?!({'|'.join(map(re.escape, palabras_clave))}))[A-Za-z0-9_\- ]+"
t_GET_TEXT = r'getText'

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
    url = p[3]
    navigate_to_url(url)
    print('El valor de la expresión es: ' + str(p[3]))

def p_command_click(p):
    'command : CLICK OPEN_PAREN TEXT CLOSE_PAREN SEMICOLON'
    element_id = p[3]
    click_element(element_id)
    print('El valor de la expresión es: ' + str(p[3]))

def p_command_text(p):
    'command : TEXT OPEN_PAREN TEXT COMMA TEXT CLOSE_PAREN SEMICOLON'
    element_id = p[3]
    text = p[5]
    set_text(element_id, text)
    print('El valor de la expresión es: ' + str(p[3]) + "->" + str(p[5]))

## define in the grammatic a command to get the text of an element
def p_command_get_text(p):
    'command : GET_TEXT OPEN_PAREN TEXT COMMA TEXT CLOSE_PAREN SEMICOLON'
    element_id = p[3]
    element_text = p[5]
    get_text(element_id, element_text)
    print('El valor de la expresión es: ' + str(p[3]))

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

driver = webdriver.Chrome()

current_url = ""

def navigate_to_url(url):
    global current_url
    current_url = url
    driver.get(url)
    sleep(1)

def get_text(element_id, element_text):
    try:
        elements = driver.find_elements(By.CLASS_NAME, element_id)
        exists = False
        while not exists:
            for element in elements:
                if element.get_attribute('innerText') == element_text:
                    exists = True
                    break
        print (exists)
        sleep(3)
    except Exception as e:
        print(f"Error al obtener el texto del elemento con ID '{element_id}': {e}")

def click_element(element_id):
    try:
        element = driver.find_element(By.ID, element_id)
        print(element)
        element.click()
        sleep(15)
    except Exception as e:
        print(f"Error al hacer clic en el elemento con ID '{element_id}': {e}")

def set_text(element_id, text):
    try:
        element = driver.find_element(By.ID, element_id)
        element.send_keys(text)
        sleep(1)
    except Exception as e:
        print(f"Error al establecer el texto en el elemento con ID '{element_id}': {e}")

# hacer un test utilizando pytest
def test_navigate_to_url():
    navigate_to_url("https://www.google.com/")
    assert current_url == "https://www.google.com/"

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)