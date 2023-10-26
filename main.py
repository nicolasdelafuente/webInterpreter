import re
from selenium import webdriver
from time import sleep
import ply.yacc as yacc
import ply.lex as lex
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
t_COMMA    = r','
t_CLICK    = r'click'
palabras_clave = ['nav', 'click']
t_TEXT   = fr"(?!({'|'.join(map(re.escape, palabras_clave))}))[A-Za-z0-9_]+"

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
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

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

parser = yacc.yacc()

driver = webdriver.Chrome()

current_url = ""

def navigate_to_url(url):
    global current_url
    current_url = url
    driver.get(url)
    sleep(3)

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
        sleep(3)
    except Exception as e:
        print(f"Error al establecer el texto en el elemento con ID '{element_id}': {e}")

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)
