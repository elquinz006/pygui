import os
from tkinter import *

# base_folder = os.getcwd()
base_folder = os.path.dirname(__file__)
base_folder = os.path.join(base_folder,'gui')
image_path = os.path.join(base_folder,'Logo.png')
print(image_path)

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

# photo = PhotoImage(file="c:/Study/python/hellopy/Logo.png")
# photo = PhotoImage(file="Logo.png")
photo = PhotoImage(file=image_path)
label2 = Label(root, image=photo)
label2.pack()

def change():
   label1.config(text="또 만나요")

   global photo2
   image_path = os.path.join(base_folder,'LogoDev.png')
   photo2 = PhotoImage(file=image_path)
   # path = image_path+"LogoDev.png"
   # print(path)
   photo2 = PhotoImage(file=image_path)
   label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
