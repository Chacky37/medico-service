import tkinter as tk

# Función que se ejecutará al presionar el botón
def saludar():
    nombre = entry.get()  # Obtiene el texto del campo de entrada
    saludo = f"¡Hola, {nombre}!"  # Crea un saludo
    label_resultado.config(text=saludo)  # Muestra el saludo en la etiqueta

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Vista Sencilla con Tkinter")  # Título de la ventana
ventana.geometry("300x200")  # Tamaño de la ventana

# Crear una etiqueta
label = tk.Label(ventana, text="¿Cómo te llamas?")
label.pack(pady=10)  # Añade la etiqueta a la ventana y agrega un espaciado

# Crear un campo de entrada
entry = tk.Entry(ventana)
entry.pack(pady=5)  # Añade el campo de entrada a la ventana

# Crear un botón
button = tk.Button(ventana, text="Saludar", command=saludar)
button.pack(pady=10)  # Añade el botón a la ventana

# Crear una etiqueta para mostrar el saludo
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)  # Añade la etiqueta de saludo

# Iniciar la aplicación
ventana.mainloop()
