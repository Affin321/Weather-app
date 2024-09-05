import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk

def get_weather(city):
    API_key = "969bc2eace5c7627e8ce1adb11c15e8d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not Found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    Temperature = weather['main']['temp'] - 273.15
    Description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"

    return (icon_url, Temperature, Description, city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, Temperature, Description, city, country = result

    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {Temperature:.2f}°C")
    description_label.configure(text=f"Description: {Description}")


def show_info():
    info_text = ("The Product Manager Accelerator Program is designed to support PM professionals "
                 "through every stage of their career. From students looking for entry-level jobs "
                 "to Directors looking to take on a leadership role, our program has helped over hundreds "
                 "of students fulfill their career aspirations.\n\n"
                 "Our Product Manager Accelerator community is ambitious and committed. Through our program, "
                 "they have learned, honed, and developed new PM and leadership skills, giving them a strong foundation "
                 "for their future endeavors.\n\n"
                 "Learn product management for free today on our YouTube channel: "
                 "https://www.youtube.com/c/drnancyli?sub_confirmation=1\n\n"
                 "Interested in PM Accelerator Pro?\n"
                 "Step 1️⃣: Attend the Product Masterclass to learn more about the program details, price, different packages, "
                 "and stay until the end to get a FREE AI Course. Learn how to create a killer product portfolio in two weeks "
                 "that will help you land any PM job (traditional or AI), even if you were laid off or have zero PM experience: "
                 "https://www.drnancyli.com/masterclass\n"
                 "Step 2️⃣: Reserve your early bird ticket and submit an application to talk to our Head of Admission.\n"
                 "Step 3️⃣: Successful applicants join our PMA Pro community to receive customized coaching!")

    messagebox.showinfo("About PM Accelerator", info_text)


root = ttk.Window(themename="morph")
root.title("Weather App")
root.geometry("400x450")


name_label = tk.Label(root, text="Affin Malik", font="Helvetica, 12", fg="grey")
name_label.pack(pady=5)


city_entry = ttk.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)


search_button = ttk.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)


location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()


info_button = ttk.Button(root, text="Info", command=show_info, bootstyle="info")
info_button.pack(pady=20)

root.mainloop()
