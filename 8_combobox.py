import tkinter.ttk as ttk
from tkinter import *
# from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]
cmbx = ttk.Combobox(root, height=5, values=values)
cmbx.pack()
cmbx.set("카드 결제일")

readonly_cmbx = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_cmbx.current(0)
readonly_cmbx.pack()

def btncmd():
   # listbox.delete(0)
   # print("리스트에는", listbox.size(), "개가 있어요.")
   # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))
   print(cmbx.get())
   print(readonly_cmbx.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
