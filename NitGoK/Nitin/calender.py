from tkinter import *
import calendar
from datetime import datetime 

def today():
    cal = calendar.month(year,month)
    screen.insert(INSERT,cal)
def show():
    year = int(spin2.get())
    mont = int(spin1.get())
    cal = calendar.month(year,mont)
    screen.delete(0.0,END)
    screen.insert(INSERT,cal)

if __name__ == "__main__":
    global now
    global tody
    global month
    global year
    root = Tk()
    root.title('Calender')
    root.geometry('300x350')
    root.configure(background='black')
    # Label(root,text='Calender',bg='olive',font='Arial 20 bold').pack(pady=10)
    date = datetime.now().date
    tody = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    frm = Frame(root,bg='orange')
    Label(frm,text='Today',font='arial 12',padx=5).pack(side=LEFT,padx=5,pady=5)
    Label(frm,text=f' {tody} / {month} / {year} ',font='arial 12').pack(side=LEFT,padx=5)
    frm.pack(pady=15)
    frm1 = Frame(root)
    Label(frm1,text='Month',font='arial 12 bold').pack(side=LEFT)
    var1 = IntVar()
    spin1 = Spinbox(frm1,from_=1,to_=12,textvariable=var1,width=5,font='arial 12')
    spin1.pack(side=LEFT,padx=5)
    var1.set(month)
    Label(frm1,text='Year',font='arial 12 bold').pack(padx=5,side=LEFT)
    var2 = IntVar()
    spin2 = Spinbox(frm1,from_=1947,to_=2030,textvariable=var2,width=5,font='arial 12')
    spin2.pack(side=LEFT,padx=5)
    var2.set(year)
    frm1.pack(pady=10)
    Button(text='Show',font='arial 10 bold', command=show).pack(pady=10)
    screen = Text(root, width=20,height=8,padx='20',pady='5')
    screen.pack()
    today()
    endfrm = Frame(root,bg='orange')
    Label(endfrm,text="By Sakthi", bg='orange').pack(side=RIGHT)
    Label(endfrm,text='©Necessary Tools').pack(side=LEFT)
    endfrm.pack(side=BOTTOM, fill=X)
    root.mainloop()
