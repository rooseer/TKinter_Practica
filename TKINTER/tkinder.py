import tkinter as tk

# Función que se ejecutará cuando se haga clic en un botón
def obtenerValor():
    texto = entrada.get()  # Obtener el valor del cuadro de entrada
    etiqueta.config(text="El nombre es: " + texto)  # Actualizar la etiqueta con el valor

# Crear una instancia de la ventana principal
ventana = tk.Tk()
ventana.title("roser ventana")

#crear una variable que tenga un texto
predeterminado ="ingresa aqui tu nombre"
# Crear un cuadro de entrada
entrada = tk.Entry(ventana)
#assignarle un texto predeterminado al cuadro predeterminado
entrada.insert(0, predeterminado)
entrada.pack()

# Crear un botón para obtener el valor ingresado
boton = tk.Button(ventana, text="Obtener Valor", command=obtenerValor)
boton.pack()

# Crear una etiqueta para mostrar el valor ingresado
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
