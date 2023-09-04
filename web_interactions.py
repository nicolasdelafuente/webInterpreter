from selenium import webdriver
from selenium.webdriver.common.by import By

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    return driver

def navigate_to_url(driver, url):
    driver.get(url)

def input_text(driver, element, text):
    element.send_keys(text)

def perform_action(driver, command):
    parts = command.split(" ")
    action = parts[0].strip()
    target = parts[1].strip()
    #value = parts[2].strip()
    print(action)
    print(target)
    #print(value)

    if action == "nav":
        navigate_to_url(driver, value)
    elif action == "input_text":
        element = driver.find_element(By.XPATH, target)
        input_text(driver, element, value)
    else:
        print(f"Comando no reconocido: {command}")

def main():
    # Inicializa el controlador de Chrome
    driver = initialize_driver()

    try:
        # Abre el archivo de comandos
        with open("comandos.txt", "r") as archivo_comandos:
            lineas = archivo_comandos.readlines()

            for linea in lineas:
                # Ejecuta el comando en función de su contenido
                comando = linea.strip()
                perform_action(driver, comando)

    except FileNotFoundError:
        print("El archivo de comandos no fue encontrado.")
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()