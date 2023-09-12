import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_prayer_time(city, country):
    
    url=f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"

    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return None

    except Exception as e:
        return f"unexcepted error occurred {e}"
    
def gui_fetch_prayer_times():
    city=city_entry.get()
    country=country_entry.get()

    if city and country:
       prayer_timing=fetch_prayer_time(city, country)
       for name, time in prayer_timing.items():
           result.insert(tk.END, f"{name}:{time}")
    else:
        messagebox.showerror("error","unable to fetch prayer times, please type city and country names")         

mainWindow = tk.Tk()
mainWindow.title("Prayer App")

frame = ttk.Frame(mainWindow, padding="20")
frame.grid(row=0, column=0)

city_label = ttk.Label(frame, text="City: ")
city_label.grid(row=0, column=0, pady=5)
city_entry= ttk.Entry(frame, width=20)
city_entry.grid(row=0, column=1, pady=5)

country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column=0, pady=5)
country_entry= ttk.Entry(frame, width=20)
country_entry.grid(row=1, column=1, pady=5)

fetch_button = ttk.Button(frame, text="Get prayer times", command=gui_fetch_prayer_times)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

result= tk.Listbox(frame, height=11, width=30)
result.grid(row=3, column=0, columnspan=2, pady=5)

mainWindow.mainloop()