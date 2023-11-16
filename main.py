#from src.lexer import lexer
from src.parser_ import parser

f = open("./entrada.txt", "r")
input_text = f.read()
print(input_text)
parser.parse(input_text)

def procesar_archivo():
    with open('./entrada.txt', 'r') as file:
        contenido = file.read()
        # Realizar operaciones con el contenido del archivo (procesamiento)

        # Ejemplo: Imprimir el contenido en consola
        print(contenido)


if __name__ == "__main__":
    procesar_archivo()