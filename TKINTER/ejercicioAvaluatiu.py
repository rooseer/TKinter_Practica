import os
import tkinter as tk
from tkinter import filedialog as quelcom
from tkinter import Toplevel
from PIL import Image, ImageTk

# Función para abrir una imagen seleccionada
def obrir_imatge():
    # Obtener el path de la imagen seleccionada
    path_imatge = quelcom.askopenfilename(initialdir=directori_imatges,
                                          title="Selecciona una imatge",
                                          filetypes=(("Imatges", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.ppm;*.pgm"), ("Tots els arxius", "*.*")))
    
    if path_imatge:
        # Crear una nueva ventana secundaria para mostrar la imagen y el path
        finestra_secundaria = Toplevel(root)
        finestra_secundaria.title("Visor d'imatges")
        
        # Mostrar el path de la imagen
        path_label = tk.Label(finestra_secundaria, text=f'Path de la imatge: {path_imatge}')
        path_label.pack()
        
        # Abrir y mostrar la imagen
        imatge_original = Image.open(path_imatge)
        imatge_original = imatge_original.resize((400, 400))  # Redimensionar la imagen si es necesario
        imatge_tk = ImageTk.PhotoImage(imatge_original)
        
        imatge_label = tk.Label(finestra_secundaria, image=imatge_tk)
        imatge_label.imatge = imatge_tk
        imatge_label.pack()
        
        # Agregar un botón para guardar la imagen con un nombre diferente
        guardar_boton = tk.Button(finestra_secundaria, text="Guardar como...", command=lambda: guardar_imatge(imatge_original))
        guardar_boton.pack()

# Función para guardar la imagen con un nombre diferente
def guardar_imatge(imatge):
    # Obtener el path y el nombre del archivo para guardar
    path_guardar = quelcom.asksaveasfilename(defaultextension=".png",
                                             filetypes=(("Imatges PNG", "*.png"),
                                                        ("Imatges JPEG", "*.jpg;*.jpeg"),
                                                        ("Todos los archivos", "*.*")))
    
    if path_guardar:
        imatge.save(path_guardar)
        tk.messagebox.showinfo("Guardado", f"La imagen se ha guardado como {path_guardar}")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestió d'imatges")

# Obtener el directorio actual del script
directori_actual = os.getcwd()

directori_imatges = os.path.join(directori_actual, './')

# Crear un botón para abrir una imagen
boton_obrir_imatge = tk.Button(root, text="Obrir Imatge", command=obrir_imatge)
boton_obrir_imatge.pack()

root.mainloop()
