from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageTk
import cv2
import numpy as np

# Initialize the main window
root = Tk()
root.title("Image Enhancer with Upscaling")
root.geometry("600x600")
root.config(bg="white")

# Global variables
original_image = None
enhanced_image = None

def open_image():
    global original_image, enhanced_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if not file_path:
        return

    # Open the selected image
    selected_image = Image.open(file_path)

    # Confirm the image selection
    confirm = messagebox.askyesno("Confirmation", "Do you want to use this image?")
    if confirm:
        # If confirmed, update the global image variables
        original_image = selected_image
        enhanced_image = original_image.copy()
        display_image(enhanced_image)
        
        # Set sliders to default values and activate them
        brightness_slider.set(1.0)
        contrast_slider.set(1.0)
        sharpness_slider.set(1.0)
        scale_slider.set(1.0)
        
        # Automatically apply enhancement to display the initial image
        enhance_image(
            brightness=brightness_slider.get(),
            contrast=contrast_slider.get(),
            sharpness=sharpness_slider.get(),
            scale=scale_slider.get()
        )
    else:
        messagebox.showinfo("Image Selection", "Please select a different image if desired.")

def display_image(img):
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

def enhance_image(brightness=1.0, contrast=1.0, sharpness=1.0, scale=1.0):
    global enhanced_image
    if original_image:
        # Adjust brightness, contrast, and sharpness
        enhancer_b = ImageEnhance.Brightness(original_image)
        img_b = enhancer_b.enhance(brightness)
        
        enhancer_c = ImageEnhance.Contrast(img_b)
        img_c = enhancer_c.enhance(contrast)
        
        enhancer_s = ImageEnhance.Sharpness(img_c)
        img_enhanced = enhancer_s.enhance(sharpness)
        
        # Upscale the image using OpenCV for more pixels
        width, height = img_enhanced.size
        new_width = int(width * scale)
        new_height = int(height * scale)
        img_cv = np.array(img_enhanced)
        img_cv = cv2.resize(img_cv, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
        enhanced_image = Image.fromarray(img_cv)

        display_image(enhanced_image)

def save_image():
    if enhanced_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if file_path:
            enhanced_image.save(file_path)
            messagebox.showinfo("Image Enhancer", "Image saved successfully!")
    else:
        messagebox.showwarning("Warning", "No enhanced image to save")

# Brightness, Contrast, Sharpness, and Scale sliders
def update_brightness(val):
    enhance_image(brightness=float(val), contrast=contrast_slider.get(), sharpness=sharpness_slider.get(), scale=scale_slider.get())

def update_contrast(val):
    enhance_image(brightness=brightness_slider.get(), contrast=float(val), sharpness=sharpness_slider.get(), scale=scale_slider.get())

def update_sharpness(val):
    enhance_image(brightness=brightness_slider.get(), contrast=contrast_slider.get(), sharpness=float(val), scale=scale_slider.get())

def update_scale(val):
    enhance_image(brightness=brightness_slider.get(), contrast=contrast_slider.get(), sharpness=sharpness_slider.get(), scale=float(val))

# UI Elements
Label(root, text="Image Enhancer with Upscaling", font=("Arial", 16), bg="white").pack(pady=10)
Button(root, text="Open Image", command=open_image, bg="#ff4f5a", fg="white", font=("Arial", 12)).pack(pady=10)

# Image display
image_label = Label(root, bg="white")
image_label.pack(pady=10)

# Sliders for Brightness, Contrast, Sharpness, and Scale
brightness_slider = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Brightness", command=update_brightness)
brightness_slider.set(1.0)
brightness_slider.pack(fill="x", padx=20, pady=5)

contrast_slider = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Contrast", command=update_contrast)
contrast_slider.set(1.0)
contrast_slider.pack(fill="x", padx=20, pady=5)

sharpness_slider = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Sharpness", command=update_sharpness)
sharpness_slider.set(1.0)
sharpness_slider.pack(fill="x", padx=20, pady=5)

# Scale slider for upscaling the image
scale_slider = Scale(root, from_=1.0, to=3.0, resolution=0.1, orient=HORIZONTAL, label="Scale (Upscale)", command=update_scale)
scale_slider.set(1.0)
scale_slider.pack(fill="x", padx=20, pady=5)

# Save button
Button(root, text="Save Image", command=save_image, bg="#ff4f5a", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()
