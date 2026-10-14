import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Cua so Tkinter dau tien")
cua_so.geometry("400x300") # rong x cao (don vi pixel)
cua_so.mainloop() # vong lap su kien, giu cua so hien thi
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Ung dung demo")
cua_so.geometry("400x300")
cua_so.resizable(False, False) # khong cho keo rong/cao
nhan = tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16))
nhan.pack(pady=20)
cua_so.mainloop()