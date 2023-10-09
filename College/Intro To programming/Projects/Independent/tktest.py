import tkinter as tk

root = tk.Tk()
root.title("First tkinter")

root.attributes('-alpha',0.5)
button = tk.Button()

greeting = tk.Label(text="Hello, World")
greeting.pack()

root.mainloop()