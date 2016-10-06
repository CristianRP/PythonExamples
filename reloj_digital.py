#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import tkinter as ttk
import time
#
root = ttk.Tk()
root.focus()
root.title("RELOJ - PYTHON")
root.config(cursor='watch')
time1 = ''
clock = ttk.Label(root, font=('ubuntu', 30, 'bold'), bg='#3C3B37', fg='white', bd=0)
clock.pack(fill='both', expand=1)
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
tick()
root.mainloop()