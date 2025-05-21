import datetime as dt
import tkinter as tk


def getTime():
    now= dt.datetime.today().strftime("%H:%M:%S")
    return now
    
def showtime():
    now= getTime()
    tag2["text"]= now



window= tk.Tk()

window.geometry("600x65")

window.title('Clock 4 Focus')

tag2= tk.Label(window, bg="#022001",fg="#356433", font="Helvetica 40")
tag2.pack(fill=tk.X)
def update_time():
    tag2["text"] = getTime()
    window.after(1000, update_time)

update_time()


window.mainloop()