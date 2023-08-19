import web_interactions

def main():
    while True:
        try:
            input_text = input("Introduce una URL o escribe 'search' para buscar: ")
        except EOFError:
            break
        if not input_text:
            print("Debes ingresar una URL o 'search'")
            continue

        command = web_interactions.parse_command(input_text)
        if command == 'search':
            search_term = input("Introduce el término de búsqueda: ")
            web_interactions.open_navigator_and_search(search_term)
        else:
            web_interactions.open_navigator_and_navigate(command)

if __name__ == '__main__':
    main()