import tkinter as tk


#funcion para definir una segunda ventana que se activa cuando se pulsa el boton    
def accio():
    ventana2= tk.Tk()
    ventana2.title("ventana 2")

    etiqueta1 =tk.Label(ventana2, text="este texto es predefinido")
    etiqueta1.pack()

# Crear una instancia de la ventana principal
ventana = tk.Tk()
# Agregar una etiqueta a la ventana
etiqueta = tk.Label(ventana, text="¡Hola, mundo!, esto es una prueba")
etiqueta.grid(row=0, column=0)  # Etiqueta en la fila 0, columna 0

# Crear un botón con medidas personalizadas
button = tk.Button(ventana, text="pincha aqui", width=10, height=1, command=accio)
button.grid(row=1, column=0)  # Botón en la fila 1, columna 0

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
