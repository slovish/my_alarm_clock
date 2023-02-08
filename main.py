import tkinter as tk
from tkinter import filedialog
import time
from playsound import playsound
import datetime


def alarm(set_alarm_timer):
    print(set_alarm_timer)
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            play_sound()
            break

def set_alarm():
    try:
        hour =int( hour_entry.get() )
        if hour >12:
            root.destroy()
        elif hour == 12:
            if is_AM:
                hour = 0
        else:
            if is_AM:
                pass
            else:
                hour += 12

        set_alarm_timer = f"{hour}:{minute_entry.get()}:{second_entry.get()}"
        alarm(set_alarm_timer)
    except Exception as e:
        print(e)

filepath = "C:\\Users\\Vishal jha\\Desktop\\intern_projects\\my_alarm_clock\\sample_tones\\tone1.mp3"

def play_sound():
   playsound(filepath)

def stop():
    root.destroy()


def choose_file():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    sound_entry.config(text= filepath.split("/")[-1])


is_AM = True

def switch():
    global is_AM
    if is_AM:
        am_pm_button.config(text="PM")
        is_AM = False
    else:
        am_pm_button.config(text="AM")
        is_AM = True


root = tk.Tk()
root.title("Alarm Clock")
root.columnconfigure(0, weight=15)
root.columnconfigure(1, weight=10)
root.columnconfigure(2, weight=10)
root.columnconfigure(3, weight=10)
root.columnconfigure(4, weight=10)


alarm_label = tk.Label(root, text="Alarm")
alarm_label.grid(row=0, column=0, sticky="Nw")
hour_label = tk.Label(root, text="HH")
hour_label.grid(row=0, column=1,pady=10, sticky="N")
minute_label = tk.Label(root, text="MM")
minute_label.grid(row=0,column=2,pady=10,sticky="N")
second_label = tk.Label(root, text="SS")
second_label.grid(row=0, column=3,pady=10, sticky="N")
am_pm_label = tk.Label(root, text="AM/PM")
am_pm_label.grid(row=0, column=4,pady=10, sticky="N")

# 2nd row

time_label = tk.Label(root, text="Time:")
time_label.grid(row=1, column=0, sticky="W")
hour_entry = tk.Entry(root, width=3)
hour_entry.grid(row=1, column=1, sticky="N")
minute_entry = tk.Entry(root, width=3)
minute_entry.grid(row=1, column=2, sticky="N")
second_entry = tk.Entry(root, width=3)
second_entry.grid(row=1, column=3, sticky="N")
am_pm_button = tk.Button(root, text="AM", command=switch)
am_pm_button.grid(row=1, column=4, sticky="N")

# 3rd row
tone_label = tk.Label(root, text="Alarm Tone")
tone_label.grid(row=2, column=0,pady=10, sticky="W")
choose_file_button = tk.Button(root, text="Choose", command=choose_file)
choose_file_button.grid(row=2 , column=4,pady=10, sticky="N")
sound_entry = tk.Label(root,text="Default: tone1", width=20)
sound_entry.grid(row=2, column=1,padx=5,pady=10, columnspan=3)
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.grid(row=3, column=1, columnspan=3, pady=10)
stop_button = tk.Button(root, text="Stop", command=stop, bg="red", fg="black")
stop_button.grid(row=4, column=1, columnspan=3, pady=10)

warning_label = tk.Label(root, text="Plaese use 12 hour format")
warning_label.grid(row=5, column=0,pady=10,columnspan=5, sticky="S")
root.mainloop()

