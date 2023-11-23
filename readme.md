## Install

pip install selenium

pip install ply

### Manual de uso

El Web Interpreter puede ejecutarse de dos formas:

- Ejecutando el programa entero haciendo uso del archivo "entrada.txt"
- Ejecutando la interfaz gráfica donde se puede cargar cada comando a mano, o cargar un archivo alojado en tu pc.

## Ejecutando Web Interprete desde main.py

- Desde la consola ejecutamos el comando:
~~~
py main.py
~~~

De esta forma ejecutaremos el programa entero, tomando como input el archivo "entrada.txt" 

## Ejecutando Web Interprete desde interfaz.py

- Desde la consola ejecutamos el comando:
~~~
py interfaz.py
~~~

Nos abrirá una interfaz donde tendremos diferentes opciones:

1- Desde el botón "Abrir archivo" podemos seleccionar un archivo desde nuestra pc (archivo .txt) con el código a ejecutar.
2- Podemos escribir a mano los comandos a ejecutar en la interfaz.
3- Desde el botón "Agregar nav" se nos abrirá otra pantalla para poder ingresar la url a donde navegar.
4- Desde el botón "Agregar text" donde podemos decirle en que lugar (XPATH) y el texto a escribir.
5- Desde el botón "Agregar click" donde podemos pasarle el XPATH del boton a clickear.
6- Desde el botón "Obtener texto" donde escribimos el XPATH del que tiene el texto que debemos comparar.
7- Desde el botón "Comparar texto" donde escribimos el texto que debería estar guardado anteriormente desde el botón "Obtener texto". 

A medida que vamos agregando los comandos veremos en la interfaz los cambios.

Con el botón "Iniciar" corremos el programa con los comandos antes agregados.


## Comandos

nav(url);  ------------------------> Navega a la url solicitada (con formato http o https)
text(XPATH, Texto_a_ingresar ); ---> Ingresa el valor del "Texto_a_ingresar" en ese XPATH
click (XPATH); --------------------> Hace click en el botón indicado como XPATH
elementText(XPATH);  --------------> Guarda el texto que se encuentre en este XPATH
assertText(texto_a_comparar); -----> Compara el texto_a_comparar con el texto anteriormente guardado en elementText(xpath)
