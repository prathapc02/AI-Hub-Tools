from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
from datetime import datetime
import numpy as np
import subprocess


def expand_window(content_frame, title):
    global current_frame
    if current_frame:
        current_frame.destroy()

    current_frame = Frame(content_frame, width=1000, height=800, bg='#000000')
    current_frame.pack_propagate(False)
    current_frame.pack(padx=20, pady=20)

    title_with_datetime = f"{title} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    root.title(title_with_datetime)

    if title == "Home":
        display_home(current_frame)
    elif title == "AI Tools":
        display_ai_tools(current_frame)
    elif title == "About":
        display_about(current_frame)
    elif title == "Essential Tools":
        display_essential_tools(current_frame)
    elif title == "About":
        display_about(current_frame)
    elif title == "Face Capture":
        capture_faces(current_frame)

def display_home(frame):
    img = Image.open("1.jpg")
    img = img.resize((750, 550), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(frame, image=img, compound="top", fg="white", bg="#000000")
    panel.image = img
    panel.pack(expand=True)

    label_font = ('Helvetica', 12, 'bold')
    text_label = Label(frame, text="AI Tools GUI \n This project incorporates features like face recognition, \nemotion detection, voice assistant, \n and voice translation into a user-friendly GUI interface.\nSome more ESSENTIAL TOOLS were also added.", font=label_font, fg="white", bg="#000000")
    text_label.pack(expand=True, fill="both")

def display_ai_tools(frame):
    notebook = ttk.Notebook(frame)
    notebook.pack(expand=True, fill='both')

    tab_info = [
        {"name": "Face Dataset Creation|", "image_path": "fdc.jpg", "button_text": "START CAPTURE", "command": lambda: capture_faces(frame)},
        {"name": "| Face Recognition |", "image_path": "fr.jpg", "button_text": "FACE RECOGNIZE", "command": recognize_faces},
        {"name": "| Emotion Detection |", "image_path": "ed.jpg", "button_text": "EMOTION DETECTION", "command": perform_third_tab_program},
        {"name": "| Voice Assistant |", "image_path": "va.webp", "button_text": "VOICE ASSISTANT", "command": launch_assistant_program},
        {"name": "| Speech Translation |", "image_path": "vt.png", "button_text": "SPEECH TRANSLATION", "command": speech_translation}
    ]

    for tab_info_item in tab_info:
        tab_frame = Frame(notebook, bg='#000000')
        notebook.add(tab_frame, text=tab_info_item["name"])

        img = Image.open(tab_info_item["image_path"])
        img = img.resize((900, 500), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(tab_frame, image=img, bg='#000000')
        panel.image = img
        panel.pack(expand=True)

        button = Button(tab_frame, text=tab_info_item["button_text"], width=20, height=2, bg="white", fg="#262626",
                        command=tab_info_item.get("command"))
        button.pack(pady=6)

# Function to launch assistant program
def launch_assistant_program():
    subprocess.Popen(['python', 'working.py'])

# Function to perform third tab program
def perform_third_tab_program():
    subprocess.Popen(['python', 'mm.py'])

# Function to display necessary tools content
def display_essential_tools(frame):
    frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
    frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

    image_commands = [
        ("dict.png", "Dictionary", command1),
        ("calcc.webp", "Calculator", command2),
        ("calendar.PNG", "Calender", command3),
        ("contact.png", "Contact Management", command4),
        ("calculator.png", "Currency-Converter", command5),
        ("weatherr.png", "Weather", command6),
        ("languages.png", "Text-Translator", command7),
        ("w2p.png", "Word To PDF", command8),
        ("camera.png", "Camera", command9),
        ("yt.png", "Youtube Video Downloader", command10)
    ]

    for i, (image_path, label_text, command) in enumerate(image_commands):
        img = Image.open(image_path)
        img = img.resize((170, 170), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        btn = Button(frame, image=img, text=label_text, compound="top", command=command, fg="black", relief=FLAT,
                     highlightbackground="black", highlightcolor="black", borderwidth=3, highlightthickness=3)
        btn.image = img
        btn.grid(row=i // 5, column=i % 5, padx=15, pady=30, sticky="nsew")


def command1():
    subprocess.Popen(['python', 'dictionary.py'])

def command2():
    subprocess.Popen(['python', 'calc.py'])

def command3():
    subprocess.Popen(['python', 'calender.py'])

def command4():
    subprocess.Popen(['python', 'Contact.py'])

def command5():
    subprocess.Popen(['python', 'currency-converter.py'])

def command6():
    subprocess.Popen(['python', 'weather.py'])

def command7():
    subprocess.Popen(['python', 'translator.py'])

def command8():
    subprocess.Popen(['python', 'convert-docx-to-pdf.py'])
def command9():
    subprocess.Popen(['python', 'rec.py'])

def command10():
    subprocess.Popen(['python', 'yt.py'])


# Function to display about content
def display_about(frame):
    # Load and display the image
    img = Image.open("abt.png")
    img = img.resize((1000, 570), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(frame, image=img, bg='#000000')
    panel.image = img
    panel.pack()

    # Add GitHub link
    github_label = Label(frame, text="", fg="white", bg="#000000")
    github_label.pack(side="left")
    github_link = Label(frame, text="My GitHub Profile", fg="blue", cursor="hand2")
    github_link.pack(side="left")
    github_link.bind("<Button-1>", lambda event: open_github())

    # Add LinkedIn link
    linkedin_label = Label(frame, text="", fg="white", bg="#000000")
    linkedin_label.pack(side="right")
    linkedin_link = Label(frame, text="My LinkedIn Profile", fg="blue", cursor="hand2")
    linkedin_link.pack(side="right")
    linkedin_link.bind("<Button-1>", lambda event: open_linkedin())

def open_linkedin():
    import webbrowser
    webbrowser.open_new("https://www.linkedin.com/in/sakthivel-m-1546a128b")

def open_github():
    import webbrowser
    webbrowser.open_new("https://github.com/Sakthirsh?tab=repositories")

# Function to capture faces
def capture_faces(frame):
    global cap, face_cascade, dataset_path

    name_window = Toplevel(root)
    name_window.title("Enter Name")
    name_window.geometry("300x100")
    name_window.configure(bg='#000000')  

    name_label = Label(name_window, text="Enter Name:", fg="white", bg="#000000")  
    name_label.pack()

    name_entry = Entry(name_window)
    name_entry.pack()

    def start_capture():
        global face_data  

        name = name_entry.get()
        dataset_path = "./face_dataset/"
        file_name = name + ".npy"

        face_data = []  

        photos_captured = 0
        photos_to_capture = 200

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame from the camera.")
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

            k = 1
            faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)

            for face in faces[:1]:
                x, y, w, h = face
                offset = 5
                face_offset = frame[y-offset:y+h+offset, x-offset:x+w+offset]
                face_selection = cv2.resize(face_offset, (100, 100))
                if photos_captured < photos_to_capture:
                    face_data.append(face_selection)
                    print("Photo", photos_captured + 1, "captured")
                    photos_captured += 1

                cv2.imshow(str(k), face_selection)
                k += 1
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow("faces", frame)

            key_pressed = cv2.waitKey(1) & 0xFF
            if key_pressed == ord('q') or photos_captured >= photos_to_capture:
                break

        if photos_captured > 0:
            face_data = np.array(face_data)
            face_data = face_data.reshape((face_data.shape[0], -1))
            np.save(dataset_path + file_name, face_data)
            print("Dataset saved at : {}".format(dataset_path + file_name))

        cap.release()
        cv2.destroyAllWindows()

        name_window.destroy()

    start_button = Button(name_window, text="Start Capture", command=start_capture, bg="#808080", fg="#262626")
    start_button.pack()

# Function to recognize faces
def recognize_faces():
    import numpy as np
    import cv2
    import os

    def distance(v1, v2):
        return np.sqrt(((v1-v2)**2).sum())

    def knn(train, test, k=5):
        dist = []
        for i in range(train.shape[0]):
            ix = train[i, :-1]
            iy = train[i, -1]
            d = distance(test, ix)
            dist.append([d, iy])

        dk = sorted(dist, key=lambda x: x[0])[:k]
        labels = np.array(dk)[:, -1]
        output = np.unique(labels, return_counts=True)
        index = np.argmax(output[1])
        return output[0][index]

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    dataset_path = "./face_dataset/"

    face_data = []
    labels = []
    class_id = 0
    names = {}

    for fx in os.listdir(dataset_path):
        if fx.endswith('.npy'):
            names[class_id] = fx[:-4]
            data_item = np.load(dataset_path + fx)
            face_data.append(data_item)
            target = class_id * np.ones((data_item.shape[0],))
            class_id += 1
            labels.append(target)
        elif fx.endswith(".jpg") or fx.endswith(".jpeg") or fx.endswith(".png"):
            name = fx.split('_')[0]
            if name not in names:
                names[name] = class_id
                class_id += 1

    face_dataset = np.concatenate(face_data, axis=0)
    face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))
    print(face_labels.shape)
    print(face_dataset.shape)
    trainset = np.concatenate((face_dataset, face_labels), axis=1)
    print(trainset.shape)

    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, frame = cap.read()
        if ret == False:
            continue
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for face in faces:
            x, y, w, h = face
            offset = 5
            face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
            face_section = cv2.resize(face_section, (100, 100))
            out = knn(trainset, face_section.flatten())
            cv2.putText(frame, names[int(out)], (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        cv2.imshow("Faces", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to display speech translation content
def speech_translation():
    subprocess.Popen(['python', 'translator_GUI.py'])

# Main Tkinter setup
root = Tk()
root.title("AI Tools GUI")
root.geometry("1200x800")
root.configure(bg='#000000')  

current_frame = None
menu_frame = Frame(root, bg="#262626")
menu_frame.pack(fill=X)

# Update function to display current date and time
def update_datetime_label():
    datetime_label.config(text=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    datetime_label.after(1000, update_datetime_label)  # Update every 1000 ms (1 second)

# Create label for displaying date and time
datetime_label = Label(root, text="", fg="white", bg="#000000")
datetime_label.pack(anchor=NE, padx=10, pady=10)

# Start updating date and time
update_datetime_label()

menu_buttons = [
    ("Home", "Home"),
    ("AI Tools", "AI Tools"),
    ("Essential Tools", "Essential Tools"),
    ("About", "About"),
]

for text, title in menu_buttons:
    btn = Button(menu_frame, text=text, bg="#262626", fg="white", command=lambda title=title: expand_window(root, title))
    btn.pack(side=LEFT, padx=10, pady=5)

expand_window(root, "Home")
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
dataset_path = "./face_dataset/"
root.mainloop()
