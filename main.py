import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk
from tkinter.messagebox import showinfo

def show_answer(inp1, inp2, operator_cb):
    val1 = int(inp1.get("1.0", tk.END))
    val2 = int(inp2.get("1.0", tk.END))

    operator = operator_cb.get()

    answer = val1 + val2

    messagebox.showwarning("Het antwoord!", answer)

r = tk.Tk()
'''
widgets are added here
'''
inp1 = tk.Text(r, height=5, width=40)
inp1.pack()

# label
label = ttk.Label(text="Plus of min?")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_operator = tk.StringVar()
operator_cb = ttk.Combobox(r, textvariable=selected_operator)

# get first 3 letters of every operator name
operator_cb['values'] = ['+', '-']

# prevent typing a value
operator_cb['state'] = 'readonly'

# place the widget
operator_cb.pack(fill=tk.X, padx=5, pady=5)

inp2 = tk.Text(r, height=5, width=40)
inp2.pack()
btn = tk.Button(r, text='Geef antwoord', width=40, command=lambda: show_answer(inp1, inp2, operator_cb))
btn.pack()
r.mainloop()