import tkinter as tk
#funcion para agregar el numero cuando se pulsa
def agregar_numero(numero):
    entrada.insert(tk.END, numero)
#funcion para el boton borrar
def delete():
    entrada.delete(0, tk.END)
#funcion para calcular, para hacer las operaciones, en casod e dar error saltara una excepcion
def calcular():
    try:
        resultado = eval(entrada.get())
        delete()
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        delete()
        entrada.insert(tk.END, "Error")
#creo la ventana
ventana = tk.Tk()
# y le pongo un titulo
ventana.title("Calculadora Roser Roman")

# Crear una entrada para los números
entrada = tk.Entry(ventana, font=("Arial", 30), justify="right")
entrada.grid(row=0, column=0, columnspan=4)

# Crear botones para los números y operaciones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

fila, columna = 1, 0
#hacer un bucle para saber que hacer en cada caso
for boton_texto in botones:
    if boton_texto == 'C':
        boton = tk.Button(ventana, text=boton_texto, padx=20, pady=20, command=delete)
    elif boton_texto == '=':
        boton = tk.Button(ventana, text=boton_texto, padx=20, pady=20, command=calcular)
    else:
        # Establece el fondo del botón como transparente
        boton = tk.Button(ventana, text=boton_texto, padx=20, pady=20, command=lambda x=boton_texto: agregar_numero(x))
    
    boton.grid(row=fila, column=columna, padx=5, pady=5, ipadx=10, ipady=10)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
#lanzar la ventana
ventana.mainloop()
