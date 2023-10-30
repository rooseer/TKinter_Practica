import sqlite3
import os
import tkinter as tk
from tkinter import messagebox

# Nombre de la base  datos y ruta al directorio donde se creará
nombre_BD = "baloncesto.db"
directorio_BD = "./db/"

# Comprobamos si el directorio existe, si no, lo creamos
if not os.path.exists(directorio_BD):
    os.makedirs(directorio_BD)

# Conectamos a la base de datos (creará la base de datos si no existe)
ruta_BD = os.path.join(directorio_BD, nombre_BD)
var_BD = sqlite3.connect(ruta_BD)

# Creamos la tabla 'jugadors' con los campos especificados
cur_BD = var_BD.cursor()
cur_BD.execute("""
    CREATE TABLE IF NOT EXISTS jugadors (
        nom TEXT,
        cognom TEXT,
        alçada REAL,
        edat INTEGER
    )
""")

# Guardamos los cambios en la base de datos y cerramos la conexión
var_BD.commit()
var_BD.close()

print(f"Base de datos '{nombre_BD}' creada en '{directorio_BD}'")

# Función para agregar datos a la base de datos
def agregar_datos():
    try:
        # Conectamos a la base de datos
        var_BD = sqlite3.connect(ruta_BD)
        cur_BD = var_BD.cursor()

        # Obtenemos los valores de las entradas
        nombre = Entry_nom.get()
        apellido = Entry_cognom.get()
        altura = Entry_alçada.get()
        edad = Entry_edat.get()

        # Insertamos los datos en la base de datos
        cur_BD.execute("INSERT INTO jugadors (nom, cognom, alçada, edat) VALUES (?, ?, ?, ?)",
                        (nombre, apellido, altura, edad))

        # Guardamos los cambios en la base de datos y cerramos la conexión
        var_BD.commit()
        var_BD.close()

        # Limpiamos las entradas después de agregar los datos
        Entry_nom.delete(0, tk.END)
        Entry_cognom.delete(0, tk.END)
        Entry_alçada.delete(0, tk.END)
        Entry_edat.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Datos agregados correctamente a la base de datos.")

    except Exception as e:
        messagebox.showerror("Error", f"Error al agregar datos a la base de datos: {str(e)}")

def mostrar_datos():
    try:
        # Conectamos a la base de datos
        var_BD = sqlite3.connect(ruta_BD)
        cur_BD = var_BD.cursor()

        # Realizamos una consulta SQL para seleccionar todos los registros de la tabla 'jugadors'
        cur_BD.execute("SELECT * FROM jugadors")
        datos = cur_BD.fetchall()  # Recuperamos todos los datos

        # Creamos una nueva ventana para mostrar  datos
        ventana_mostrar = tk.Toplevel(ventana)
        ventana_mostrar.title("Datos en la Base de Datos")

        # Creamos un widget de Texto para mostrar los datos
        texto_datos = tk.Text(ventana_mostrar)
        texto_datos.pack()

        # Formateamos los datos y los agregamos al widget de Texto
        for dato in datos:
            texto_datos.insert(tk.END, f"Nombre: {dato[0]}\nApellido: {dato[1]}\nAltura: {dato[2]}\nEdad: {dato[3]}\n\n")

        # Cerramos la conexión a la base de datos
        var_BD.close()

    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar datos de la base de datos: {str(e)}")

# Crear la ventana principal de la GUI
ventana = tk.Tk()
ventana.title("Ingresar Datos a la Base de Datos")

# Crear las etiquetas y entradas para cada campo
label_nom = tk.Label(ventana, text="Nombre:")
Entry_nom = tk.Entry(ventana)

label_cognom = tk.Label(ventana, text="Apellido:")
Entry_cognom = tk.Entry(ventana)

label_alçada = tk.Label(ventana, text="Altura:")
Entry_alçada = tk.Entry(ventana)

label_edat = tk.Label(ventana, text="Edad:")
Entry_edat = tk.Entry(ventana)

# Crear el botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar Datos", command=agregar_datos)

# Colocar elementos en la ventana
label_nom.grid(row=0, column=0)
Entry_nom.grid(row=0, column=1)

label_cognom.grid(row=1, column=0)
Entry_cognom.grid(row=1, column=1)

label_alçada.grid(row=2, column=0)
Entry_alçada.grid(row=2, column=1)

label_edat.grid(row=3, column=0)
Entry_edat.grid(row=3, column=1)

boton_agregar.grid(row=4, columnspan=2)

boton_mostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos)

# Colocar el botón en la ventana
boton_mostrar.grid(row=5, columnspan=2)

# Iniciar la GUI
ventana.mainloop()
