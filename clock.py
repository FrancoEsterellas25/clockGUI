import datetime as dt
import tkinter as tk
import locale


def update_time():
    tag2.config(text= getTime())
    tagdate.config(text=getDay())
    window.after(1000, update_time)

my_schedule = {
    'lunes' : [('9:00','13:00','Programación')],
    'martes' : [('9:00','12:00','Matemática Machine Learning')],
    'miércoles' : [('9:00','12:00','Intro. Ciencias Biomédicas'),('14:00','16:00','Filosofía')],
    'jueves' : [('9:00','12:00','Matemática Machine Learning')],
    'viernes' : [('9:00','12:00','taller de Internet')]
}

def isinclass():
    now= dt.datetime.today()
    day= now.strftime("%A")
    hour= now.time()

    if day in my_schedule:
        for start_class, end_class, class_name in my_schedule[day]:
            start = dt.datetime.strptime(start_class, "%H:%M").time()
            end = dt.datetime.strptime(end_class, "%H:%M").time()

            if hour > start and hour < end:
                return True, class_name

    return False, ""
        
def showyellow():
    in_class, subject = isinclass()
    if in_class:
        window.geometry("600x138")
        tag2.config(bg="#d9af2f",fg="#E4D593")
        tagdate.config(bg="#d9af2f",fg="#E4D593")
        tagclass.config(text=f"En clase {subject}...",bg="#d9af2f",fg="#E4D593")
        window.configure(bg="#d9af2f")
    else:
        tag2.config(bg="#022001",fg="#356433")
        tagdate.config(bg="#022001",fg="#356433")
        tagclass.pack_forget()
        window.geometry("600x150")
        window.configure(bg="#022001")

    window.after(5000, showyellow)

def go_sleep():
    window.geometry("600x218")
    tag2.config(bg="#151939", fg="#afbfff")
    tagdate.config(bg="#151939", fg="#afbfff")
    tagclass.config(text="Durmiendo... zzz", bg="#151939", fg="#afbfff")
    tagclass.pack(fill=tk.X)
    window.configure(bg="#151939")


def getTime():
    now= dt.datetime.today().strftime("%H:%M:%S")
    return now
def getDay():
    locale.setlocale(locale.LC_TIME, "Spanish_Spain")
    currentdate= dt.date.today()  
    printed_date= currentdate.strftime("%A, %d de %B")
    return printed_date

window= tk.Tk()
window.configure(bg="#022001")

window.geometry("600x158")

window.title('Clock 4 Focus')

tag2= tk.Label(window, bg="#022001",fg="#356433", font="Helvetica 40")
tag2.pack(fill=tk.X)
tagdate= tk.Label(window,bg="#022001",fg="#3C673A", font="Helvetica 25")
tagdate.pack(fill=tk.X)

tagclass= tk.Label(window, text="", fg="#022001", font=("Helvetica",15))
tagclass.pack(fill=tk.X)

sleepbuton= tk.Button(text="Go sleep", command= go_sleep, bg="white")
sleepbuton.pack(side="bottom", pady=10)

update_time()
showyellow()

window.mainloop()