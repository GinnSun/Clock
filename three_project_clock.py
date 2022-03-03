from tkinter import *
import time
import tkinter as tk

def Time():
    clock_current = time.strftime('%H : %M : %S')
    date_current = time.strftime('%d.%m.%Y')
    date_clock['text']=date_current
    clock['text'] = clock_current
    clock.after(200, Time)
win = tk.Tk()
win.config(bg='#30D5C8')
win.geometry('500x250+620+290')
win.title('clock')
win.resizable(False,False)
photo = PhotoImage(file='clock_icon_128908.png')
win.iconphoto(False, photo)
clock = tk.Label(win,text='' ,font=('times',60, 'bold'),bg='#30D5C8' )
clock.grid(row=2, column=2, pady=25, padx=50)
date_clock = tk.Label(win, text='', font=('times',30, 'bold'), bg='#30D5C8')
date_clock.grid(row=3, column=2)
Time()
options=tk.Label(win,text="hours        minutes        seconds",font="times 15 bold", bg='#30D5C8')
options.grid(row=1,column=2)
win.mainloop()
