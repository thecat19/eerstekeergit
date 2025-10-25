import tkinter as tk
from tkinter import messagebox 

def show_answer(inp1, inp2):
    val1 = int(inp1.get("1.0", tk.END))
    val2 = int(inp2.get("1.0", tk.END))
    answer = val1 + val2
    messagebox.showwarning("Het antwoord!", answer)

r = tk.Tk()
'''
widgets are added here
'''
inp1 = tk.Text(r, height=5, width=40)
inp1.pack()



inp2 = tk.Text(r, height=5, width=40)
inp2.pack()
btn = tk.Button(r, text='Geef antwoord', width=40, command=lambda: show_answer(inp1, inp2))
btn.pack()
r.mainloop()