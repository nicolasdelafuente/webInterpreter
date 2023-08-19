from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import lexer_parser 

def parse_command(input_text):
    # Analizar el texto de entrada utilizando el analizador léxico y sintáctico.
    result = lexer_parser.parser.parse(input_text)
    # El resultado es el comando parseado ('URL' o 'SEARCH').
    return result

def open_navigator_and_search(search_term):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/")

    search_box = driver.find_element(by=By.NAME, value="q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Espera a que se carguen los resultados de la búsqueda
    WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(by=By.CLASS_NAME, value="gsc-results")
    )

    # Prevent Chrome from closing after the search
    driver.execute_script("window.onbeforeunload = function() {return false;}")

def open_navigator_and_navigate(url):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(f"http://{url}")

