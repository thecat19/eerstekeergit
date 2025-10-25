import tkinter as tk
r = tk.Tk()
'''
widgets are added here
'''
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()