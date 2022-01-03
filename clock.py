import time
from tkinter import *
canvas = Tk()
canvas.title('Digital Clock - by Kaviya Sri')
canvas.geometry('585x50')
canvas.resizable(False,False)
label = Label(canvas, font=('Arial', 28, 'bold'), bg = 'green', fg = 'white')
label.grid(row = 1, column = 1)
def clock():
    inp = time.strftime('%H Hours %M Minutes %S Seconds')
    label.config(text = inp)
    label.after(100,clock)
clock()
canvas.mainloop()