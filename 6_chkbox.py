from tkinter import *
# from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
   # listbox.delete(0)
   # print("리스트에는", listbox.size(), "개가 있어요.")
   # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))
   print(chkvar.get())
   print(chkvar2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
