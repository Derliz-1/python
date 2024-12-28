import tkinter as tk

# Función para manejar la acción de los botones
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Función para realizar el cálculo
def calculate():
    try:
        result = eval(entry.get())  # eval evalúa la expresión matemática
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Función para borrar la entrada
def clear():
    entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear una entrada (entry) para mostrar la operación y el resultado
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Definir los botones de la calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4),  # Botón para borrar
]

# Crear y agregar los botones a la ventana
for (text, row, col, *extra) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), bg="#4CAF50", fg="white", command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), bg="#f44336", fg="white", command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), command=lambda val=text: button_click(val))
    
    btn.grid(row=row, column=col)

# Ejecutar la aplicación
root.mainloop()
