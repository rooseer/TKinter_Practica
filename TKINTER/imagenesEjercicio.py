import tkinter as tk
from PIL import Image, ImageTk

# Rutas de las imágenes
imagenes = [
    "imagen1.jpg",
    "imagen2.jpg",
    "imagen3.jpg",
    "imagen4.jpg",
    "imagen5.jpg",
]

# Funciones para cambiar de imagen
def siguiente_imagen():
    global imagen_actual
    if imagen_actual < len(imagenes) - 1:
        imagen_actual += 1
        mostrar_imagen()
        actualizar_etiqueta()

        # Si llegamos a la última imagen, desactivamos el botón Siguiente
        if imagen_actual == len(imagenes) - 1:
            btn_siguiente.config(state=tk.DISABLED)
        # Al avanzar, siempre habilitamos el botón Anterior
        btn_anterior.config(state=tk.NORMAL)

def anterior_imagen():
    global imagen_actual
    if imagen_actual > 0:
        imagen_actual -= 1
        mostrar_imagen()
        actualizar_etiqueta()

        # Si volvemos a la primera imagen, desactivamos el botón Anterior
        if imagen_actual == 0:
            btn_anterior.config(state=tk.DISABLED)
        # Al retroceder, siempre habilitamos el botón Siguiente
        btn_siguiente.config(state=tk.NORMAL)

# Función para mostrar la imagen actual
def mostrar_imagen():
    imagen = Image.open(imagenes[imagen_actual])
    imagen.thumbnail((400, 400))
    foto = ImageTk.PhotoImage(imagen)
    label_imagen.config(image=foto)
    label_imagen.image = foto

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Función para actualizar la etiqueta de información
def actualizar_etiqueta():
    etiqueta_info.config(text=f"Imagen {imagen_actual + 1} de {len(imagenes)}")

# Inicialización de la ventana
ventana = tk.Tk()
ventana.title("Visor de Imágenes")
ventana.geometry("600x500")

# Variables
imagen_actual = 0

# Botones
btn_anterior = tk.Button(ventana, text="Anterior", command=anterior_imagen)
btn_anterior.pack(side=tk.LEFT, padx=10)
btn_siguiente = tk.Button(ventana, text="Siguiente", command=siguiente_imagen)
btn_siguiente.pack(side=tk.RIGHT, padx=10)
btn_salir = tk.Button(ventana, text="Salir", command=salir)
btn_salir.pack(side=tk.BOTTOM, pady=10)

# Etiqueta para mostrar la imagen
label_imagen = tk.Label(ventana)
label_imagen.pack(expand=True)

# Etiqueta para mostrar la información de la imagen
etiqueta_info = tk.Label(ventana, text="")
etiqueta_info.pack(side=tk.LEFT, padx=10, pady=10)

# Mostrar la primera imagen y actualizar la etiqueta de información
mostrar_imagen()
actualizar_etiqueta()

# Desactivar el botón Anterior al inicio
btn_anterior.config(state=tk.DISABLED)

ventana.mainloop()
