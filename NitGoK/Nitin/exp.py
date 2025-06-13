from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

def expand_window(content_frame, title):
    global current_frame
    if current_frame:
        current_frame.destroy()

    current_frame = Frame(content_frame, width=1000, height=600, bg='#000000')  # Setting background color to black
    current_frame.pack_propagate(False)
    current_frame.pack(padx=10, pady=10)

    if title == "Home":
        display_home(current_frame)
    elif title == "AI Tools":
        display_ai_tools(current_frame)
    elif title == "Necessary Tools":
        display_necessary_tools(current_frame)
    elif title == "About":
        display_about(current_frame)

def display_home(frame):
    img = Image.open("1.jpg")
    img = img.resize((300, 300), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(frame, image=img, text="AI Tools GUI", compound="top", fg="white", bg="#000000")  # Setting background color to black
    panel.image = img
    panel.pack(expand=True)

def display_ai_tools(frame):
    # Create a notebook (tabbed layout)
    notebook = ttk.Notebook(frame)
    notebook.pack(expand=True, fill='both')

    # Define image paths and button texts for each tab
    tab_info = [
        {"image_path": "1.jpg", "button_text": "Button 1"},
        {"image_path": "1.jpg", "button_text": "Button 2"},
        {"image_path": "1.jpg", "button_text": "Button 3"},
        {"image_path": "1.jpg", "button_text": "Button 4"},
        {"image_path": "1.jpg", "button_text": "Button 5"}
    ]

    for i, tab_info in enumerate(tab_info):
        tab_frame = Frame(notebook, bg='#000000')  # Setting background color to black
        notebook.add(tab_frame, text=f'Tab {i+1}')

        # Display image
        img = Image.open(tab_info["image_path"])
        img = img.resize((300, 300), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(tab_frame, image=img, bg='#000000')  # Setting background color to black
        panel.image = img
        panel.pack(expand=True)

        # Display button at the bottom center
        button_frame = Frame(tab_frame, bg='#000000')  # Setting background color to black
        button_frame.pack(side=BOTTOM, pady=10)

        btn = Button(button_frame, text=tab_info["button_text"], width=15, height=2, bg="#808080", fg="#262626")  # Change bg color to grey
        btn.pack(pady=6)

def display_necessary_tools(frame):
    # Create a list of image paths
    image_paths = ["1.jpg", "1.jpg", "1.jpg", "1.jpg", "1.jpg",
                   "1.jpg", "1.jpg", "1.jpg", "1.jpg", "1.jpg"]

    # Create 10 buttons with associated image above each button
    for i, image_path in enumerate(image_paths):
        img = Image.open(image_path)
        img = img.resize((100, 100), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        # Create a label to display the image
        label_img = Label(frame, image=img, bg="#000000")
        label_img.image = img
        label_img.grid(row=i // 5 * 2, column=i % 5, padx=5, pady=5)

        # Create a button below the image
        btn = Button(frame, text=f"Button {i+1}", width=10, height=2, bg="#808080", fg="#262626")
        btn.grid(row=i // 5 * 2 + 1, column=i % 5, padx=5, pady=5)
def display_about(frame):
    label = Label(frame, text="Author: Your Name\nAddress: Your Address", font=("Arial", 16), fg="white", bg="#000000")  # Setting background color to black
    label.pack(expand=True)

w = Tk()
w.geometry('900x600')
w.configure(bg='#000000')  # Setting background color to black
w.resizable(1, 1)
w.title('Toggle Expanding Window')

current_frame = None

menu_frame = Frame(w, width=200, bg='#808080')
menu_frame.pack(side=LEFT, fill=Y)

options = ["Home", "AI Tools", "Necessary Tools", "About"]

for option in options:
    btn = Button(menu_frame, text=option, width=15, height=2, bg='#808080', fg='#262626',  # Change bg color to grey
                 command=lambda o=option: expand_window(w, o))
    btn.pack(pady=10)

expand_window(w, "Home")

w.mainloop()
