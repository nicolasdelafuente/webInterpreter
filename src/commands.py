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

def click_element(element_id):
    try:
        element = driver.find_element(By.XPATH, element_id)
        print(element)
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

def get_element_text(element):
    try:
        return element.get_attribute('innerText')
    except Exception as e:
        print(f"Error al obtener el texto del elemento: {e}")
        return None

def assert_element_text(element_text, expected_text):
    return element_text == expected_text

def get_text(element_, element_text):
    try:
        elements = find_elements(element_)
        
        assert_ = False

        for element in elements:
            text = get_element_text(element)
            if text is not None and assert_element_text(text, element_text):
                assert_ = True

        print(f"'{element_text}' encontrado: '{assert_}'")

    except Exception as e:
        print(f"Error al obtener el texto del elemento'{element_}': {e}")
