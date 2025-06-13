import sys

try:
    from tkinter import *
    from tkinter import messagebox, filedialog
    import threading
    from docx import Document
    import pdfplumber
except ModuleNotFoundError as error:
    print(error)
    input("Press Any Key To Exit .. ")
    sys.exit()


class PDFToWord:
    def __init__(self) -> None:
        # Window Design
        self.root = Tk()
        self.root.title("PDF2Word")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)
        self.root.configure(bg="#FFF")
        self.root.iconbitmap("pdf-icon.ico")
        # Vars
        self.pdf_var = StringVar()
        self.word_var = StringVar()
        # Title Label
        self.title_label = Label(self.root, text="Convert PDF To Word", bg="#FFF", font=("roboto", 20, "bold"))
        self.title_label.pack(fill="x", pady=20)
        # Entries
        pdf_entry = Entry(self.root, width=35, highlightbackground="black", state="disabled",
                          highlightcolor="black", highlightthickness=2, textvariable=self.pdf_var)
        pdf_entry.place(x=30, y=120)

        word_entry = Entry(self.root, width=35, highlightbackground="black", state="disabled",
                           highlightcolor="black", highlightthickness=2, textvariable=self.word_var)
        word_entry.place(x=30, y=160)
        # Buttons
        pdf_button = Button(self.root, text="PDF", width=10, borderwidth=2, bg="black"
                            , fg="white", font=("verdana", 10, "bold"), command=self.get_pdf)
        pdf_button.place(x=265, y=118)

        word_button = Button(self.root, text="Save", width=10, borderwidth=2, bg="black"
                             , fg="white", font=("verdana", 10, "bold"), command=self.save)
        word_button.place(x=265, y=158)

        convert_button = Button(self.root, text="Convert", width=10, borderwidth=2, bg="black"
                                , fg="white", font=("verdana", 10, "bold"), command=self.convert_thread)
        convert_button.place(x=150, y=220)

        clear_button = Button(self.root, text="Clear", width=10, borderwidth=2, bg="black"
                              , fg="white", font=("verdana", 10, "bold"), command=self.clear)
        clear_button.place(x=265, y=220)

        exit_button = Button(self.root, text="Exit", width=10, borderwidth=2, bg="black"
                             , fg="white", font=("verdana", 10, "bold"), command=self.exit_)
        exit_button.place(x=30, y=220)
        self.root.mainloop()

    def get_pdf(self):
        self.pdf_var.set(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))

    def save(self):
        self.word_var.set(filedialog.asksaveasfilename(defaultextension=".docx", 
                                                       filetypes=[("Word files", "*.docx")]))

    def convert(self):
        if self.pdf_var.get() == "":
            messagebox.showerror("Error", "Choose PDF File")
        elif self.word_var.get() == "":
            messagebox.showerror("Error", "Choose Path to Save Word File")
        else:
            try:
                pdf_path = self.pdf_var.get()
                word_path = self.word_var.get()

                # Extract text from PDF and save to Word document
                with pdfplumber.open(pdf_path) as pdf:
                    doc = Document()
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            doc.add_paragraph(text)
                    doc.save(word_path)

                messagebox.showinfo("Converted", "Conversion Successful")
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "An error occurred during conversion")

    def convert_thread(self):
        threading.Thread(target=self.convert).start()

    def clear(self):
        self.pdf_var.set("")
        self.word_var.set("")

    def exit_(self):
        check = messagebox.askyesno("Exit", "Do you want to exit?")
        if check:
            self.root.destroy()


if __name__ == '__main__':
    PDFToWord()
