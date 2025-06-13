from PIL import Image, ImageTk
from tkinter import filedialog, Tk, Button, messagebox, Toplevel, Label

def upscale_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return
    
    # Open the original image
    original_img = Image.open(file_path)
    
    # Get original dimensions
    original_width, original_height = original_img.size

    # Define target HD resolution (1920x1080)
    hd_width, hd_height = 5000, 4531

    # If the original image is smaller than HD, upscale it
    if original_width < hd_width or original_height < hd_height:
        # Upscale the image to HD resolution using the 'lanczos' filter for high-quality resizing
        enhanced_img = original_img.resize((hd_width, hd_height), Image.LANCZOS)
    else:
        # If the image is already larger, keep the original resolution
        enhanced_img = original_img
    
    # Save the enhanced image
    enhanced_path = file_path.replace(".", "_upscaled.")
    enhanced_img.save(enhanced_path)
    
    # Display success message
    messagebox.showinfo("Enhancement Complete", "Successfully Enhanced the image to HD!")

    # Show before and after images
    show_before_after(original_img, enhanced_img)

def show_before_after(original_img, enhanced_img):
    # Create a new window to display both images
    comparison_window = Toplevel(root)
    comparison_window.title("Before and After")
    
    # Resize images for display if they’re too large
    max_size = (300, 300)
    original_img.thumbnail(max_size)
    enhanced_img.thumbnail(max_size)

    # Convert images to ImageTk format for displaying in Tkinter
    original_img_tk = ImageTk.PhotoImage(original_img)
    enhanced_img_tk = ImageTk.PhotoImage(enhanced_img)

    # Display the original image
    Label(comparison_window, text="Before").pack()
    Label(comparison_window, image=original_img_tk).pack()

    # Display the enhanced image
    Label(comparison_window, text="After").pack()
    Label(comparison_window, image=enhanced_img_tk).pack()

    # Keep references to the images to prevent garbage collection
    comparison_window.original_img_tk = original_img_tk
    comparison_window.enhanced_img_tk = enhanced_img_tk

# Basic Tkinter UI to trigger enhancement
root = Tk()
root.title("Image Enhancement")
root.geometry("300x200")

Button(root, text="Image Enhancer", command=upscale_image).pack(pady=20)
root.mainloop()
