import yt_dlp
import os
from tkinter import *
from tkinter import messagebox

def download_video():
    link = url_entry.get()
    selected_resolution = resolution_var.get()

    if not link:
        messagebox.showwarning("Warning", "Please enter a YouTube video URL")
        return
    if not selected_resolution:
        messagebox.showwarning("Warning", "Please select a resolution")
        return

    # Set up the download directory
    download_dir = "downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    try:
        print("Saving to:", os.path.abspath(download_dir))  # ✅ Add this line

        ydl_opts = {
            'format': f'bestvideo[height<={selected_resolution[:-1]}]+bestaudio/best[height<={selected_resolution[:-1]}]',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Success", f"Video downloaded successfully to: {os.path.abspath(download_dir)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

def update_resolutions():
    resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
    resolution_menu["menu"].delete(0, "end")
    for res in resolutions:
        resolution_menu["menu"].add_command(label=res, command=lambda value=res: resolution_var.set(value))
    resolution_var.set(resolutions[0])

# Setting up the Tkinter window
w = Tk()
w.title("YouTube Video Downloader")
w.geometry("500x350")
w.config(bg="white")

Label(w, text="Enter URL of Video:", bg="white", font=("Arial", 12)).pack(pady=10)
url_entry = Entry(w, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

Button(w, text="Fetch Resolutions", command=update_resolutions, bg="#ff4f5a", fg="white", font=("Arial", 10)).pack(pady=10)

resolution_var = StringVar(w)
resolution_var.set("")
Label(w, text="Select Resolution:", bg="white", font=("Arial", 12)).pack(pady=5)
resolution_menu = OptionMenu(w, resolution_var, "")
resolution_menu.config(width=20, font=("Arial", 10))
resolution_menu.pack(pady=5)

Button(w, text="Download", command=download_video, bg="#ff4f5a", fg="white", font=("Arial", 12)).pack(pady=20)

w.mainloop()
