## Install

pip install selenium

pip install ply

## Archivos importantes

## Main

Importa módulos necesarios, como re (para expresiones regulares), selenium (para automatización web), time (para agregar retrasos), ply.yacc y ply.lex (para crear un analizador y un lexer), y selenium.webdriver.common.by (para definir localizadores de elementos).

Define un conjunto de nombres de tokens para el lexer, incluyendo palabras clave como NAV, URL, ID, CLICK, y operadores como ASSIGN, OPEN_PAREN y CLOSE_PAREN. También define expresiones regulares para coincidir con URLs y IDs de elementos.

Define las reglas del lexer para tokenizar el código de entrada.

Configura un analizador básico utilizando PLY, definiendo reglas de gramática para comandos como NAV, CLICK y ASSIGN. Especifica cómo se analizan estos comandos y qué acciones tomar cuando se encuentra cada comando.

Define funciones de manejo de errores tanto para el lexer como para el analizador para manejar errores de sintaxis.

Inicializa un controlador de WebDriver para Chrome utilizando Selenium.

Define funciones para navegar a una URL, hacer clic en un elemento y establecer texto en un elemento. Estas funciones utilizan Selenium para interactuar con la página web.

Lee la entrada desde un archivo llamado "entrada.txt".

Analiza la entrada utilizando el analizador definido.

## Parser

El analizador sintáctico se utiliza para analizar la estructura del lenguaje específico de dominio que se ha definido previamente. 

Las partes clave del archivo "parsetab.py" son:

La definición de la versión del analizador generado y el método de análisis (LALR).

La firma del analizador sintáctico (_lr_signature) que describe cómo se reconocen y procesan los tokens y las reglas de la gramática.

Las acciones que se deben tomar cuando se encuentran ciertos tokens durante el análisis.

Las reglas de producción (_lr_productions) que definen cómo se deben construir las estructuras de datos a medida que se analiza la entrada.
