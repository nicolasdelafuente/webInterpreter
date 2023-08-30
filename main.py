import web_interactions

def main():
    nombre_archivo = "codigo.txt"  # Cambia "archivo.txt" por el nombre de tu archivo
    #while True:
        # try:
        #     input_text = input("Introduce una URL o escribe 'search' para buscar: ")
        # except EOFError:
        #     break
        # if not input_text:
        #     print("Debes ingresar una URL o 'search'")
        #     continue
    try:
        with open(nombre_archivo, "r") as archivo:
            print(nombre_archivo)
            lineas = archivo.readlines()  # Lee todas las líneas del archivo
            for linea in lineas:
                elementos = linea.strip().split(";")  # Divide la línea en elementos separados por ;
    # Procesa cada elemento como desees
            for elemento in elementos:
                print(elemento)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print("Ocurrió un error:", e)

        # command = web_interactions.parse_command(input_text)
        # if command == 'search':
        #     search_term = input("Introduce el término de búsqueda: ")
        #     web_interactions.open_navigator_and_search(search_term)
        # else:
        #     web_interactions.open_navigator_and_navigate(command)

if __name__ == '__main__':
    main()