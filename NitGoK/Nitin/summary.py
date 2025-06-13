import tkinter as tk
from tkinter import simpledialog, messagebox
from transformers import pipeline

# Load the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(input_text, max_length=130, min_length=30):
    """
    Summarize the text using a transformer-based summarization model.
    """
    try:
        # Generate summary using the summarizer pipeline
        result = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        return f"An error occurred: {str(e)}"

def summarize_input():
    # Open a dialog box to get input text from the user
    input_text = simpledialog.askstring("Input Text", "Enter the text to summarize:")

    if not input_text:
        messagebox.showwarning("No Input", "Please enter some text to summarize.")
        return

    try:
        # Summarize the input text
        summary = summarize_text(input_text)
        messagebox.showinfo("Summarized Output", summary)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Text Summarizer")
root.geometry("400x200")

# Label for the app title
title_label = tk.Label(root, text="Text Summarizer", font=("Helvetica", 16))
title_label.pack(pady=20)

# Button to trigger summarization
summarize_button = tk.Button(root, text="Summarize", width=20, height=2, bg="white", fg="#262626", command=summarize_input)
summarize_button.pack(pady=20)

# Run the main loop
root.mainloop()
