import sys

try:
    from tkinter import *
    from tkinter import messagebox, filedialog
    import threading
    import comtypes.client
except ModuleNotFoundError as error:
    print(error)
    input("Press Any Key To Exit .. ")
    sys.exit()


class PPTToPDF:
    def __init__(self) -> None:
        # Window Design
        self.root = Tk()
        self.root.title("PPT2PDF")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)
        self.root.configure(bg="#FFF")
        self.root.iconbitmap("pdf-icon.ico")
        # Vars
        self.ppt_var = StringVar()
        self.pdf_var = StringVar()
        # Title Label
        self.title_label = Label(self.root, text="Convert PPT To PDF", bg="#FFF", font=("roboto", 20, "bold"))
        self.title_label.pack(fill="x", pady=20)
        # Entries
        ppt_entry = Entry(self.root, width=35, highlightbackground="black", state="disabled",
                          highlightcolor="black", highlightthickness=2, textvariable=self.ppt_var)
        ppt_entry.place(x=30, y=120)

        pdf_entry = Entry(self.root, width=35, highlightbackground="black", state="disabled",
                          highlightcolor="black", highlightthickness=2, textvariable=self.pdf_var)
        pdf_entry.place(x=30, y=160)
        # Buttons
        ppt_button = Button(self.root, text="PPT", width=10, borderwidth=2, bg="black"
                            , fg="white", font=("verdana", 10, "bold"), command=self.get_ppt)
        ppt_button.place(x=265, y=118)

        pdf_button = Button(self.root, text="Save", width=10, borderwidth=2, bg="black"
                            , fg="white", font=("verdana", 10, "bold"), command=self.save)
        pdf_button.place(x=265, y=158)

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

    def get_ppt(self):
        self.ppt_var.set(filedialog.askopenfilename(filetypes=[("PowerPoint Files", "*.ppt;*.pptx")]))

    def save(self):
        self.pdf_var.set(filedialog.askdirectory())

    def convert(self):
        if self.ppt_var.get() == "":
            messagebox.showerror("Error", "Choose a PPT File")
        elif self.pdf_var.get() == "":
            messagebox.showerror("Error", "Choose a Save Path")
        else:
            try:
                powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
                powerpoint.Visible = 1
                presentation = powerpoint.Presentations.Open(self.ppt_var.get())
                pdf_path = f"{self.pdf_var.get()}/output.pdf"
                presentation.SaveAs(pdf_path, 32)  # 32 = ppSaveAsPDF
                presentation.Close()
                powerpoint.Quit()
                messagebox.showinfo("Converted", "Conversion Successful")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def convert_thread(self):
        threading.Thread(target=self.convert).start()

    def clear(self):
        self.ppt_var.set("")
        self.pdf_var.set("")

    def exit_(self):
        check = messagebox.askyesno("Exit", "Do you want to exit?")
        if check:
            self.root.destroy()
        else:
            pass


if __name__ == '__main__':
    PPTToPDF()
