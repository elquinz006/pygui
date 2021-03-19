import time
import tkinter.ttk as ttk
from tkinter import *
# from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# prgsbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# prgsbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# prgsbar.start(10)
# prgsbar.pack()

# def btncmd():
#    # listbox.delete(0)
#    # print("리스트에는", listbox.size(), "개가 있어요.")
#    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))
#    prgsbar.stop()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
prgsbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
prgsbar2.pack()

def btncmd2():
   for i in range(1, 101):
      time.sleep(0.01)

      p_var2.set(i)
      prgsbar2.update()

btn = Button(root, text="중지", command=btncmd2)
btn.pack()

root.mainloop()
