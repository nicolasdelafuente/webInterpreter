from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import lexer_parser 

def parse_command(input_text):
    # Analizar el texto de entrada utilizando el analizador léxico y sintáctico.
    result = lexer_parser.parser.parse(input_text)
    # El resultado es el comando parseado ('URL' o 'SEARCH').
    return result

def open_navigator_and_search(search_term):
    driver = initialize_driver()
    navigate_to_google(driver)
    perform_search(driver, search_term)

def open_navigator_and_navigate(url):
    search_term = input("Ahora, introduce el término de búsqueda: ")
    driver = initialize_driver()
    navigate_to_url(driver, url)
    perform_search(driver, search_term)
    # Prevent Chrome from closing after the search
    driver.execute_script("window.onbeforeunload = function() {return false;}")

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    return driver

def navigate_to_google(driver):
    driver.get("https://www.google.com/")

def navigate_to_url(driver, url):
    driver.get(f"http://{url}")

def perform_search(driver, search_term):
    search_box = driver.find_element(by=By.NAME, value="q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Espera a que se carguen los resultados de la búsqueda
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gsc-results"))
    )

