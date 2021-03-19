from tkinter import *
# from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="Select Menu").pack()

bgr_var = IntVar()
btn_bgr1 = Radiobutton(root, text="햄버거", value=1, variable=bgr_var)
btn_bgr2 = Radiobutton(root, text="치즈버거", value=2, variable=bgr_var)
btn_bgr3 = Radiobutton(root, text="치킨버거", value=3, variable=bgr_var)

btn_bgr1.pack()
btn_bgr2.pack()
btn_bgr3.pack()

label2 = Label(root, text="Select Drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
   # listbox.delete(0)
   # print("리스트에는", listbox.size(), "개가 있어요.")
   # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))
   print(bgr_var.get())
   print(drink_var.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
