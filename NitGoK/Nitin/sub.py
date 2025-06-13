from tkinter import *
from PIL import ImageTk,Image

w=Tk()
w.geometry('1500x800')
w.configure(bg='#262626')#12c4c0')
w.resizable(0,0)
w.attributes('-fullscreen', True)
w.title('Toggle Menu')


def default_home():
    f2=Frame(w,width=900,height=1080,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='AI TOOL',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',100))
    l2.place(x=500,y=400)
       
def home():
    f1.destroy()
    f2=Frame(w,width=1920,height=1080,bg='#262626')
    f2.place(x=0,y=45)
    img = Image.open("1.jpg")
    img = img.resize((1920, 1080), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.pack()
    l2=Label(f2,text='Home',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    toggle_win()
 

def acer():
    f1.destroy()
    f2=Frame(w,width=1920,height=1080,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Acer',fg='black',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    img = Image.open("1.jpg")
    img = img.resize((1920, 1080), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.pack()
    toggle_win()
    
   
    

def dell():
    f1.destroy()
    f2=Frame(w,width=1920,height=1080,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Dell',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=320,y=150-45)
    img = Image.open("1.jpg")
    img = img.resize((1920, 1080), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.pack()
    toggle_win()

def asus():
    f1.destroy()
    f2=Frame(w,width=1920,height=1080,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Asus',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=320,y=150-45)
    img = Image.open("1.jpg")
    img = img.resize((1920, 1080), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.pack()
    toggle_win()

def apple():
    f1.destroy()
    f2=Frame(w,width=1920,height=1080,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Apple',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=320,y=150-45)
    img = Image.open("1.jpg")
    img = img.resize((1920, 1080), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.pack()
    toggle_win()

def acer():
    f1.destroy()
    f2=Frame(w,width=1920,height=1080,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Acer',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=32,y=150-45)
    img = Image.open("1.jpg")
    img = img.resize((1920, 1080), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(image=img)
    panel.image = img
    panel.pack()
    toggle_win()


def toggle_win():
    global f1
    f1=Frame(w,width=300,height=5000,bg='#12c4c0')
    f1.place(x=0,y=0)
    
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'H O M E','#0f9d9a','#12c4c0',home)
    bttn(0,117,'A C E R','#0f9d9a','#12c4c0',acer)
    bttn(0,154,'D E L L','#0f9d9a','#12c4c0',dell)
    bttn(0,191,'A S U S','#0f9d9a','#12c4c0',asus)
    bttn(0,228,'A P P L E','#0f9d9a','#12c4c0',apple)
    bttn(0,265,'A C E R','#0f9d9a','#12c4c0',acer)

    #
    def dele():
        f1.destroy()
        b2=Button(w,image=img1,
               command=toggle_win,
               border=0,
               bg='#262626',
               activebackground='#262626')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    

default_home()

img1 = ImageTk.PhotoImage(Image.open("open.png"))

global b2
b2=Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626')
b2.place(x=5,y=8)


w.mainloop()
