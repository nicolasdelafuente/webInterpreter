import tkinter as tk
from tkinter import filedialog
import subprocess
from tkinter.scrolledtext import ScrolledText

class EditorEjecutor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor y Ejecutor")

        self.create_widgets()

    def create_widgets(self):
        abrir_button = tk.Button(self, text="Abrir archivo", command=self.abrir_archivo)
        abrir_button.pack()

        self.entrada_text = tk.Text(self, height=20, width=60)
        self.entrada_text.pack()

        self.salida_text = ScrolledText(self, height=10, width=60, bg="#D3D3D3")
        self.salida_text.pack()

        correr_button = tk.Button(self, text="Iniciar", command=self.correr_main)
        correr_button.pack()

        botones_frame = tk.Frame(self)
        botones_frame.pack()

        self.create_button(botones_frame, "Agregar nav", self.agregar_nav, bg="lightblue")
        self.create_button(botones_frame, "Agregar text", self.agregar_text, bg="lightgreen")
        self.create_button(botones_frame, "Agregar click", self.agregar_click, bg="lightyellow")
        self.create_button(botones_frame, "Obtener texto", self.obtener_text, bg="lightpink")
        self.create_button(botones_frame, "Comparar texto", self.comparar_text, bg="lightcoral")

        botones_frame.pack(side=tk.TOP, anchor='n')

    def create_button(self, frame, text, command, **kwargs):
        button = tk.Button(frame, text=text, command=command, **kwargs)
        button.pack(side=tk.LEFT, padx=10, pady=10)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                contenido = file.read()
                self.entrada_text.delete(1.0, tk.END)
                self.entrada_text.insert(tk.END, contenido)

    def guardar_archivo(self):
        contenido = self.entrada_text.get(1.0, tk.END)
        with open('entrada.txt', 'w') as file:
            file.write(contenido)

    def correr_main(self):
        self.guardar_archivo()
        try:
            result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
            self.salida_text.delete(1.0, tk.END)
            self.salida_text.insert(tk.END, result.stdout)
            if result.stderr:
                self.salida_text.insert(tk.END, "\nError:\n")
                self.salida_text.insert(tk.END, result.stderr)
        except Exception as e:
            self.salida_text.insert(tk.END, f"\nError al ejecutar el script: {str(e)}")

    def mostrar_ventana(self, titulo, mensaje, ancho=400, alto=200):
        ventana = tk.Toplevel(self)
        ventana.title(titulo)
        ventana.geometry(f"{ancho}x{alto}")
        mensaje_label = tk.Label(ventana, text=mensaje, padx=10, pady=10)
        mensaje_label.pack()

    def agregar_widget(self, titulo, campos, callback):
        def agregar_final():
            values = [entry.get() for entry in entries]
            callback(*values)
            window.destroy()

        window = tk.Toplevel(self)
        window.title(titulo)
        window.geometry("400x150")

        entries = []
        for campo in campos:
            label = tk.Label(window, text=f"Escriba {campo}:")
            label.pack()
            entry = tk.Entry(window, width=50)
            entry.pack()
            entries.append(entry)

        agregar_button = tk.Button(window, text="Agregar", command=agregar_final)
        agregar_button.pack()

    def agregar_nav(self):
        self.agregar_widget("Agregar nav", ["la URL"], self.agregar_nav_final)

    def agregar_nav_final(self, url):
        self.entrada_text.insert(tk.END, f"nav ({url});\n")

    def agregar_text(self):
        self.agregar_widget("Agregar text", ["el Xpath del input", "el texto"], self.agregar_text_final)

    def agregar_text_final(self, xpath, texto):
        self.entrada_text.insert(tk.END, f"text({xpath}, {texto});\n")

    def agregar_click(self):
        self.agregar_widget("Agregar click", ["el Xpath del botón"], self.agregar_click_final)

    def agregar_click_final(self, xpath):
        self.entrada_text.insert(tk.END, f"click ({xpath});\n")

    def obtener_text(self):
        self.agregar_widget("Obtener texto", ["el Xpath del texto"], self.obtener_text_final)

    def obtener_text_final(self, xpath):
        self.entrada_text.insert(tk.END, f"elementText({xpath});\n")
    
    def comparar_text(self):
        self.agregar_widget("Comparar texto", ["el texto a comparar"], self.comparar_text_final)

    def comparar_text_final(self, texto):
        self.entrada_text.insert(tk.END, f"assertText({texto});\n")

if __name__ == "__main__":
    app = EditorEjecutor()
    app.mainloop()
