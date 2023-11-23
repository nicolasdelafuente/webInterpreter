from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

current_url = ""


def navigate_to_url(url):
    global current_url
    current_url = url
    driver.get(url)
    sleep(3)

textos = ""

def guardar_texto(texts):
    global textos
    textos = texts

def assert_text(text):
    exists = False
    for t in textos:
        if t == text:
            exists = True
    if exists:
        print(f"El texto '{text}' es correcto")
    else:
        print(f"El texto '{text}' es incorrecto")

def get_element_text(element_id):
    try:
        elements = driver.find_elements(By.XPATH, element_id)
        # obtener el texto de todos los elementos y guardarlos en una lista
        text_elements = []
        for element in elements:
            text = element.get_attribute('innerText')
            text_elements.append(text)
        return text_elements
    except Exception as e:
        print(f"Error al obtener el texto del elemento con ID '{element_id}': {e}")

def click_element(element_id):
    try:
        element = driver.find_element(By.XPATH, element_id)
        element.click()
        sleep(3)
    except Exception as e:
        print(f"Error al hacer clic en el elemento con ID '{element_id}': {e}")

def set_text(element_id, text):
    try:
        element = driver.find_element(By.XPATH, element_id)
        element.send_keys(text)
        sleep(3)
    except Exception as e:
        print(f"Error al establecer el texto en el elemento con ID '{element_id}': {e}")

def find_elements(xpath):
    try:
        elements = driver.find_elements(By.XPATH, xpath)
        return elements
    except Exception as e:
        print(f"Error al encontrar elementos con la expresión XPath '{xpath}': {e}")
        return []
