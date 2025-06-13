from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Initialize main application window
main = Tk()
main.title("Weather App")
main.geometry("900x500+300+200")
main.resizable(False, False)

# Set application icon
image_icon = PhotoImage(file="logo.png")
main.iconphoto(False, image_icon)

# Function to get weather and display it
def get_weather():
    city = textfield.get()
    try:
        # Geocode the city to obtain location
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        
        # Check if the location is found
        if location is None:
            messagebox.showerror("Weather App", "City not found. Please try another city.")
            return
        
        # Get the timezone of the location
        obj = TimezoneFinder()
        timezone = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        # Get local time in the found timezone
        home = pytz.timezone(timezone)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        # Fetch weather data using the OpenWeather API
        api_url = (
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid=3af5b8038d2bba6c74977113680191f2"
        )
        json_data = requests.get(api_url).json()
        
        # Check if the API call was successful
        if json_data.get("cod") != 200:
            messagebox.showerror("Weather App", "Unable to fetch weather data. Please try again.")
            return
        
        # Extract data from the API response
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        
        # Update labels with weather data
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description.capitalize())
        p.config(text=f"{pressure} hPa")
    
    except Exception as e:
        # Generic error handling
        messagebox.showerror("Weather App", "An unexpected error occurred. Please try again.")

# Search box setup
Search_image = PhotoImage(file="searchm.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(
    main,
    justify="center",
    width=17,
    font=("poppins", 25, "bold"),
    bg="#404040",
    border=0,
    fg="white",
)
textfield.place(x=50, y=40)
textfield.focus()
textfield.bind("<Return>", lambda event: get_weather())

search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(
    image=search_icon,
    borderwidth=0,
    cursor="hand2",
    bg="#404040",
    command=get_weather,
)
myimage_icon.place(x=400, y=34)

# Logo setup
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=130)

# Bottom box setup
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time display setup
name = Label(main, font=("arial", 15, "bold"))
name.place(x=40, y=100)
clock = Label(main, font=("Helvetica", 20))
clock.place(x=40, y=130)

# Weather data labels
label1 = Label(
    main, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label1.place(x=120, y=400)

label2 = Label(
    main, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label2.place(x=250, y=400)

label3 = Label(
    main, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label3.place(x=430, y=400)

label4 = Label(
    main, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label4.place(x=650, y=400)

# Weather data values
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=230)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=200)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=680, y=430)

# Run the application
main.mainloop()
