import tkinter as tk
from tkinter import filedialog
import subprocess

def abrir_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            contenido = file.read()
            entrada_text.delete(1.0, tk.END)  # Limpiar el texto anterior si lo hay
            entrada_text.insert(tk.END, contenido)

def guardar_archivo():
    contenido = entrada_text.get(1.0, tk.END)
    with open('entrada.txt', 'w') as file:
        file.write(contenido)

def correr_main():
    guardar_archivo()
    subprocess.run(['python', 'main.py'])  # Ejecutar el script main.py

def mostrar_ventana(titulo, mensaje, ancho=400, alto=200):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}")
    mensaje_label = tk.Label(ventana, text=mensaje, padx=10, pady=10)
    mensaje_label.pack()

def agregar_nav():
    def agregar_nav_final():
        url = url_entry.get()
        entrada_text.insert(tk.END, f"nav ({url});\n")
        nav_window.destroy()

    nav_window = tk.Toplevel(root)
    nav_window.title("Agregar nav")
    nav_window.geometry("400x100")
    url_label = tk.Label(nav_window, text="Escriba la URL:")
    url_label.pack()
    url_entry = tk.Entry(nav_window, width=50)
    url_entry.pack()
    agregar_button = tk.Button(nav_window, text="Agregar", command=agregar_nav_final)
    agregar_button.pack()

def agregar_text():
    def agregar_text_final():
        xpath = xpath_entry.get()
        texto = texto_entry.get()
        entrada_text.insert(tk.END, f"text({xpath}, {texto});\n")
        text_window.destroy()

    text_window = tk.Toplevel(root)
    text_window.title("Agregar text")
    text_window.geometry("400x150")
    xpath_label = tk.Label(text_window, text="Escriba el Xpath del input:")
    xpath_label.pack()
    xpath_entry = tk.Entry(text_window, width=50)
    xpath_entry.pack()
    texto_label = tk.Label(text_window, text="Escriba el texto:")
    texto_label.pack()
    texto_entry = tk.Entry(text_window, width=50)
    texto_entry.pack()
    agregar_button = tk.Button(text_window, text="Agregar", command=agregar_text_final)
    agregar_button.pack()

def agregar_click():
    def agregar_click_final():
        xpath = xpath_entry.get()
        entrada_text.insert(tk.END, f"click ({xpath});\n")
        click_window.destroy()

    click_window = tk.Toplevel(root)
    click_window.title("Agregar click")
    click_window.geometry("400x100")
    xpath_label = tk.Label(click_window, text="Escriba el Xpath del botón:")
    xpath_label.pack()
    xpath_entry = tk.Entry(click_window, width=50)
    xpath_entry.pack()
    agregar_button = tk.Button(click_window, text="Agregar", command=agregar_click_final)
    agregar_button.pack()

def agregar_getText():
    def agregar_getText_final():
        xpath = xpath_entry.get()
        texto = texto_entry.get()
        entrada_text.insert(tk.END, f"getText({xpath}, {texto});\n")
        getText_window.destroy()

    getText_window = tk.Toplevel(root)
    getText_window.title("Agregar getText")
    getText_window.geometry("400x150")
    xpath_label = tk.Label(getText_window, text="Escriba el Xpath del texto:")
    xpath_label.pack()
    xpath_entry = tk.Entry(getText_window, width=50)
    xpath_entry.pack()
    texto_label = tk.Label(getText_window, text="Escriba el texto a comparar:")
    texto_label.pack()
    texto_entry = tk.Entry(getText_window, width=50)
    texto_entry.pack()
    agregar_button = tk.Button(getText_window, text="Agregar", command=agregar_getText_final)
    agregar_button.pack()

root = tk.Tk()
root.title("Editor y Ejecutor")

abrir_button = tk.Button(root, text="Abrir archivo", command=abrir_archivo)
abrir_button.pack()

entrada_text = tk.Text(root, height=20, width=60)
entrada_text.pack()

correr_button = tk.Button(root, text="Correr main", command=correr_main)
correr_button.pack()

botones_frame = tk.Frame(root)
botones_frame.pack()

nav_button = tk.Button(botones_frame, text="Agregar nav", command=agregar_nav, bg="lightblue")
nav_button.pack(side=tk.LEFT, padx=10, pady=10)

text_button = tk.Button(botones_frame, text="Agregar text", command=agregar_text, bg="lightgreen")
text_button.pack(side=tk.LEFT, padx=10, pady=10)

click_button = tk.Button(botones_frame, text="Agregar click", command=agregar_click, bg="lightyellow")
click_button.pack(side=tk.LEFT, padx=10, pady=10)

getText_button = tk.Button(botones_frame, text="Agregar getText", command=agregar_getText, bg="lightpink")
getText_button.pack(side=tk.LEFT, padx=10, pady=10)

botones_frame.pack(side=tk.TOP, anchor='n')

root.mainloop()