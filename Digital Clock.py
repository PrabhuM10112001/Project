from tkinter import *
from  datetime import datetime


#window Configuration
window = Tk() 
window.title("Digital Clock")
window.geometry('350x150')
window.resizable(width=False, height=False)

def Clock():
    time = datetime.now()
    hour = time.strftime("%H : %M : %S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")
    l1.configure(text=hour)
    l1.after(1000,Clock)
    l2.configure(text=weekday + "  " + str(day) + "/" + str(month) + "/" + str(year) )

    

l1= Label(window, text = "12: 40: 05" , font=('Arial 50'),  bg = "#c0c0c0",  fg= "#000080")
l1.grid(row=0, column=0)

l2 = Label(window, text = "Saturaday", font=('Arial 20'), fg = "#000080" )
l2.grid(row=1, column=0)

Clock()

window.mainloop()
