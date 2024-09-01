import tkinter as tk
from tkinter import messagebox
import math

# Create the main application window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")

# Memory storage
memory = 0

# Create the display
display = tk.Entry(root, font=('Arial', 24), borderwidth=5, relief="ridge", justify='right')
display.grid(row=0, column=0, columnspan=5, pady=20)

# Define button click functionality
def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(value))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def backspace():
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text[:-1])

def sqrt():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def reciprocal():
    try:
        result = 1 / float(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def power():
    try:
        base = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, f'{base}**')
    except:
        messagebox.showerror("Error", "Invalid Input")

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    global memory
    display.insert(tk.END, memory)

def memory_add():
    global memory
    try:
        memory += float(display.get())
        clear_display()
    except:
        messagebox.showerror("Error", "Invalid Input")

def memory_subtract():
    global memory
    try:
        memory -= float(display.get())
        clear_display()
    except:
        messagebox.showerror("Error", "Invalid Input")

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('√', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('1/x', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('⌫', 4, 4)
]

for (text, row, col) in buttons:
    if text == '⌫':
        action = backspace
    elif text == '√':
        action = sqrt
    elif text == '^':
        action = power
    elif text == '1/x':
        action = reciprocal
    elif text == '=':
        action = calculate
    else:
        action = lambda x=text: button_click(x)
    tk.Button(root, text=text, width=10, height=3, command=action).grid(row=row, column=col)

# Memory buttons
tk.Button(root, text='M+', width=10, height=3, command=memory_add).grid(row=5, column=0)
tk.Button(root, text='M-', width=10, height=3, command=memory_subtract).grid(row=5, column=1)
tk.Button(root, text='MR', width=10, height=3, command=memory_recall).grid(row=5, column=2)
tk.Button(root, text='MC', width=10, height=3, command=memory_clear).grid(row=5, column=3)

# Clear button
tk.Button(root, text='C', width=10, height=3, command=clear_display).grid(row=5, column=4)

# Keyboard binding
def key_event(event):
    key = event.keysym
    if key.isdigit() or key in ['period']:
        button_click(key)
    elif key in ['plus', 'minus', 'asterisk', 'slash']:
        button_click(event.char)
    elif key == 'Return':
        calculate()
    elif key == 'BackSpace':
        backspace()
    elif key == 'Escape':
        clear_display()

root.bind('<Key>', key_event)

# Run the application
root.mainloop()
