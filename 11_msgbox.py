import time
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msgbox
# from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 기차 예매 시스템
def info():
   msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
   msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
   msgbox.showerror("에러", "결제 오류가 발생하였습니다.")

def okcancel():
   msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아 동반석입니다. 예매하시겠습니까?")

def retrycancel():
   msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 하시겠습니까?")

def yesnocalcel():
   response = msgbox.askyesnocancel(title=None, message="선택하세요")
   print("응답", response)
   if response == 1:
      print("예")
   elif response == 0:
      print("아니오")
   else:
      print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel , text="확인 취소").pack()
Button(root, command=retrycancel, text="확인 취소").pack()

Button(root, command=yesnocalcel, text="확인 취소 아니오").pack()



root.mainloop()
