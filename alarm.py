import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

def set_alarm():
    alarm_time = entry.get()

    try:
        alarm_time = time.strptime(alarm_time, '%H:%M')
    except ValueError:
        messagebox.showerror("Error", "Invalid, Please use HH:MM.")
        return

    current_time = time.localtime()
    alarm_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                   alarm_time.tm_hour, alarm_time.tm_min, 0, 0, 0, -1))

    time_difference = time.mktime(alarm_time) - time.mktime(current_time)

    if time_difference <= 0:
        alarm_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday + 1,
                                       alarm_time.tm_hour, alarm_time.tm_min, 0, 0, 0, -1))
        time_difference = time.mktime(alarm_time) - time.mktime(current_time)

    root.after(int(time_difference * 1000), trigger_alarm)

def trigger_alarm():
    messagebox.showinfo("Alarm", "Time's up!")

root = tk.Tk()
root.title("Simple Alarm Clock")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter alarm time (HH:MM):")
label.grid(column=0, row=0, columnspan=2, pady=10)

entry = ttk.Entry(frame)
entry.grid(column=0, row=1, columnspan=2, pady=10)

set_button = ttk.Button(frame, text="Set Alarm", command=set_alarm)
set_button.grid(column=0, row=2, columnspan=2, pady=10)

root.mainloop()
