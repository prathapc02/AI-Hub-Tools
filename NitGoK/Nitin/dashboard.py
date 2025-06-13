import os
from tkinter import *

def launch(file_name):
    os.system(f"python {file_name}")

root = Tk()
root.title("AI Hub - All Tools")
root.geometry("400x600")
root.configure(bg="white")

Label(root, text="AI Hub - Tool Launcher", font=("Arial", 18, "bold"), fg="blue", bg="white").pack(pady=20)

buttons = [
    ("YouTube Downloader", "YD.py"),
    ("Weather App", "weather.py"),
    ("Currency Converter", "currency-converter.py"),
    ("PDF to PPT", "convert-pdf-to-ppt.py"),
    ("Translator", "translator.py"),
    ("Image Enhancer", "imgenha.py"),
    ("Calculator", "calculator.py"),
    ("Calendar", "calender.py"),
    ("Face Detection", "fdc.py"),
    ("Contact Book", "Contact.py"),
    ("PDF to DOC", "convert-pdf-docx.py"),
    ("DOC to PDF", "convert-docx-to-pdf.py"),
    ("Background Remove", "imgbckrm.py"),

]

for text, file in buttons:
    Button(root, text=text, width=30, command=lambda f=file: launch(f)).pack(pady=5)

root.mainloop()
