import time
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
   listbox.insert(tk.END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
