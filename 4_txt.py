from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")
# root.geometry("640x480+50+50")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력")
# root.resizable(False, False)

def btncmd():
   print(txt.get("1.0", END))
   print(e.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
