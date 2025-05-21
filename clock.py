import datetime as dt
import tkinter as tk
import locale

def getTime():
    now= dt.datetime.today().strftime("%H:%M:%S")
    return now
def getDay():
    locale.setlocale(locale.LC_TIME, "Spanish_Spain")
    currentdate= dt.date.today()  
    printed_date= currentdate.strftime("%A, %d de %B")
    return printed_date

window= tk.Tk()

window.geometry("600x110")

window.title('Clock 4 Focus')

tag2= tk.Label(window, bg="#022001",fg="#356433", font="Helvetica 40")
tag2.pack(fill=tk.X)
tagdate= tk.Label(window,bg="#022001",fg="#3C673A", font="Helvetica 25")
tagdate.pack(fill=tk.X)


def update_time():
    tag2.config(text= getTime())
    tagdate.config(text=getDay())
    window.after(1000, update_time)

update_time()


window.mainloop()