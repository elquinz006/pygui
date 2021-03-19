import tkinter as tk
from tkinter import Listbox, filedialog
# from typing import Text
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import var
from numpy.lib.polynomial import roots
import pandas as pd

df = pd.read_csv(
    'c:/Study/TASS/2021.03.15.TASSmotion_vF/inp/CUBE_jyg_vec.dat', skiprows=[1], delim_whitespace=True)

# hdr = list(df.columns.values)
hdr = []
# print(hdr[0])
# plotlist = ["NODE_MIX_LEVEL(9)", "NODE_MIX_LEVEL(10)"]
            # "NODE_MIX_LEVEL(11)", "NODE_MIX_LEVEL(12)"]

# df.plot(x="TIME", y=plotlist)
# plt.show()

# Xx = df["TIME"]
# Yy = df["CTL_CORE_POWER_FRACTION"]
# df.plot(x="TIME", y=["CTRL_GROUP_RESULT(5)", "CTRL_GROUP_RESULT(6)"])
# plt.show()

def openfile():
   global hdr
   filename = filedialog.askopenfilename(parent=root)
   # f = open(filename)
   # f.read()
   df = pd.read_csv(filename, skiprows=[1], delim_whitespace=True)
   header = list(df.columns.values)
   print(header[0])

   hdr = header

   mylistbox = tk.Listbox(root,width=600,height=400)
   mylistbox.bind('<<ListboxSelect>>',CurSelect)
   mylistbox.place(x=0,y=0)

   for items in hdr:
      mylistbox.insert(tk.END, items)


root = tk.Tk()
geo = root.geometry
geo("600x400+000+000")

def CurSelect(event):
   selection = mylistbox.curselection()[0]
   print(hdr[selection])

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

mylistbox = tk.Listbox(root,width=600,height=400)
mylistbox.bind('<<ListboxSelect>>',CurSelect)
mylistbox.place(x=0,y=0)

for items in hdr:
   mylistbox.insert(tk.END, items)

# print("In th, ", hdr)
# print(type(hdr))

# variable = tk.StringVar(root)
# variable.set("Time")

# w = tk.OptionMenu(root, variable, "Time")
# w.pack()

root.config(menu=menubar)
root.mainloop()
