from PIL import Image, ImageTk
from tkinter import filedialog, Tk, Button, messagebox, Toplevel, Label
from rembg import remove
import io

def remove_background():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return
    
    try:
        # Open the original image
        with open(file_path, "rb") as img_file:
            original_data = img_file.read()

        # Use rembg to remove the background
        processed_data = remove(original_data)

        # Convert the result to a PIL image
        processed_img = Image.open(io.BytesIO(processed_data))

        # Save the background-removed image
        output_path = file_path.replace(".", "_no_bg.")
        processed_img.save(output_path, format="PNG")
        
        # Display success message
        messagebox.showinfo("Background Removal Complete", f"Background removed successfully!\nSaved at {output_path}")

        # Show before and after images
        original_img = Image.open(file_path)
        show_before_after(original_img, processed_img)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_before_after(original_img, processed_img):
    # Create a new window to display both images
    comparison_window = Toplevel(root)
    comparison_window.title("Before and After")
    
    # Resize images for display if they’re too large
    max_size = (300, 300)
    original_img.thumbnail(max_size)
    processed_img.thumbnail(max_size)

    # Convert images to ImageTk format for displaying in Tkinter
    original_img_tk = ImageTk.PhotoImage(original_img)
    processed_img_tk = ImageTk.PhotoImage(processed_img)

    # Display the original image
    Label(comparison_window, text="Before").pack()
    Label(comparison_window, image=original_img_tk).pack()

    # Display the processed image
    Label(comparison_window, text="After").pack()
    Label(comparison_window, image=processed_img_tk).pack()

    # Keep references to the images to prevent garbage collection
    comparison_window.original_img_tk = original_img_tk
    comparison_window.processed_img_tk = processed_img_tk

# Basic Tkinter UI to trigger background removal
root = Tk()
root.title("Background Remover")
root.geometry("300x200")

Button(root, text="Remove Background", command=remove_background).pack(pady=20)
root.mainloop()
