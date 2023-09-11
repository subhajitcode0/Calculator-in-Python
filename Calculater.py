import tkinter as tk

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget for displaying the input and output
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '00',
    
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create special buttons for clear and calculate
tk.Button(window, text='C', width=5, height=2, command=clear).grid(row=5, column=0)
tk.Button(window, text='=', width=5, height=2, command=calculate).grid(row=5, column=1, columnspan=3)

# Start the GUI main loop
window.mainloop()
