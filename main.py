import ply.lex as lex
import ply.yacc as yacc
from selenium import webdriver

# Definición de tokens
tokens = [
    'NAV',
    'URL',
    'ID',
    'TEXT',
    'CLICK',
    'SEMICOLON',
    'ASSIGN',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'COMMA',
]

# Reglas para tokens
t_NAV = r'nav'
t_URL = r'https?://[^\s"]+|"[^\s"]+"'
t_ID = r'//input\[@id="[a-zA-Z0-9_\-]+"\]'
t_CLICK = r'click'
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_CLOSE_PAREN = r'\)'
t_OPEN_PAREN = r'\('
t_COMMA = r','
t_TEXT = r'(\'[^\']*\'|"[^"]*")'

# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

# Función para manejar errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)


# Reglas de sintaxis
def p_commands(p):
    '''commands : commands command
                | command'''
    if len(p) == 2:
        p[0] = [p[1]]
        print(p[0]) 
    else:
        p[0] = p[1] + [p[2]]

def p_command_nav(p):
    'command : NAV OPEN_PAREN URL CLOSE_PAREN SEMICOLON'
    p[0] = ('NAV_ACTION', p[3])
    print(p[0]) 

def p_command_assignment(p):
    'command : ID ASSIGN TEXT SEMICOLON'
    p[0] = ('ASSIGNMENT', p[1], p[3])

def p_command_click(p):
    'command : CLICK OPEN_PAREN ID CLOSE_PAREN SEMICOLON'
    p[0] = ('CLICK_ACTION', p[3])

def p_command_text(p):
    'command : TEXT OPEN_PAREN ID COMMA TEXT CLOSE_PAREN SEMICOLON'
    p[0] = ('TEXT_ACTION', p[3], p[5])


def p_error(p):
    if p:
        lineno = p.lineno
        column = find_column(p)
        print(f"Error sintáctico en la línea {lineno}, columna {column}: No se pudo reconocer la estructura de comandos.")
        print(f"Token erroneo: '{p.value}'")
    else:
        print("Error sintáctico: No se pudo reconocer la estructura de comandos.")

# Función para encontrar la columna donde ocurrió el error
def find_column(token):
    line_start = lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Construir el analizador léxico
lexer = lex.lex()

parsed_code = parsed_code = '''
nav("https://campus-act.unahur.edu.ar/login/index.php");
username = "//input[@id='username']";
text(username, "35970083");
password = "//input[@id='password']";
text(password, "FlorSe");
button = "//button[@id='loginbtn']";
click(button);
'''



# Manejo de las acciones semánticas
driver = webdriver.Chrome()

current_url = ""

def navigate_to_url(url):
    global current_url
    current_url = url
    driver.get(url)

def click_element(element_id):
    try:
        element = driver.find_element_by_xpath(element_id)
        element.click()
    except Exception as e:
        print(f"Error al hacer clic en el elemento con ID '{element_id}': {e}")

def set_text(element_id, text):
    try:
        element = driver.find_element_by_xpath(element_id)
        element.send_keys(text)
    except Exception as e:
        print(f"Error al establecer el texto en el elemento con ID '{element_id}': {e}")


variables = {}

parser = yacc.yacc()
parsed_code = ''.join(parsed_code.splitlines())
parsed_commands = parser.parse(parsed_code)

for command in parsed_commands:
    if isinstance(command, tuple) and len(command) == 3:
        action_type, var_name, var_value = command[0], command[1], command[2]
        if action_type == 'ASSIGNMENT':
            variables[var_name] = var_value
        elif action_type == 'NAV_ACTION':
            navigate_to_url(var_value)
        elif action_type == 'CLICK_ACTION':
             click_element(var_value)
        elif action_type == 'TEXT_ACTION':
            element_id, text_value = var_name, var_value
            set_text(element_id, text_value)
