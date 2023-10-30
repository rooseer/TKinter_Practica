import tkinter as tk
from tkinter import messagebox

def show_message_box(type):
    global last_clicked
    result = None
    if type == 'askyesno':
        result = messagebox.askyesno('Títol finestra', 'Missatge')
    elif type == 'askquestion':
        response = messagebox.askquestion('Títol finestra', 'Missatge')
        result = 'Sí' if response == 'yes' else 'No'
    elif type == 'askokcancel':
        result = messagebox.askokcancel('Títol finestra', 'Missatge')
        result = 'Sí' if result else 'No'
    elif type == 'showinfo':
        messagebox.showinfo('Títol finestra', 'Missatge')
    elif type == 'showwarning':
        messagebox.showwarning('Títol finestra', 'Missatge')
    elif type == 'showerror':
        messagebox.showerror('Títol finestra', 'Missatge')
    
    if result is not None:
        last_clicked = result

def show_last_clicked():
    label.config(text=f'Últim clic: {last_clicked}')

root = tk.Tk()
root.title('Finestra Principal')

last_clicked = 'N/A'
label = tk.Label(root, text=f'Últim clic: {last_clicked}')
label.pack()

askyesno_button = tk.Button(root, text='askyesno', command=lambda: show_message_box('askyesno'))
askyesno_button.pack()

askquestion_button = tk.Button(root, text='askquestion', command=lambda: show_message_box('askquestion'))
askquestion_button.pack()

askokcancel_button = tk.Button(root, text='askokcancel', command=lambda: show_message_box('askokcancel'))
askokcancel_button.pack()

showinfo_button = tk.Button(root, text='showinfo', command=lambda: show_message_box('showinfo'))
showinfo_button.pack()

showwarning_button = tk.Button(root, text='showwarning', command=lambda: show_message_box('showwarning'))
showwarning_button.pack()

showerror_button = tk.Button(root, text='showerror', command=lambda: show_message_box('showerror'))
showerror_button.pack()

show_last_clicked_button = tk.Button(root, text='Mostra l\'últim clic', command=show_last_clicked)
show_last_clicked_button.pack()

root.mainloop()
