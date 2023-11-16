from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

current_url = ""


def navigate_to_url(url):
    global current_url
    current_url = url
    driver.get(url)
    sleep(15)

def get_text(element_class, element_text):
    try:
        elements = driver.find_elements(By.XPATH, element_class)
        
        assert_ = False

        for element in elements:
            if (element.get_attribute('innerText') == element_text) :
                assert_ = True        
        
        print (f"'{element_text}' encontrado: '{assert_}'")
    
    except Exception as e:
        print(f"Error al obtener el texto del elemento de la CLASE '{element_class}': {e}")

def click_element(element_id):
    try:
        element = driver.find_element(By.XPATH, element_id)
        print(element)
        element.click()
        sleep(10)
    except Exception as e:
        print(f"Error al hacer clic en el elemento con ID '{element_id}': {e}")

def set_text(element_id, text):
    try:
        element = driver.find_element(By.XPATH, element_id)
        element.send_keys(text)
        sleep(10)
    except Exception as e:
        print(f"Error al establecer el texto en el elemento con ID '{element_id}': {e}")
