import tkinter as tk
from datetime import datetime, timedelta

def calculate_sleep_time():
    bed_time = bed_time_entry.get()
    wake_time = wake_time_entry.get()

    # Convert time to datetime objects
    bed_time = datetime.strptime(bed_time, "%H:%M")
    wake_time = datetime.strptime(wake_time, "%H:%M")

    # Calculate sleep duration
    if wake_time < bed_time:
        wake_time += timedelta(days=1)
    sleep_duration = wake_time - bed_time

    # Display sleep duration
    sleep_duration_label.config(text=f"Sleep Duration: {sleep_duration}")

    # Suggest bedtime routine
    routine_start = bed_time - timedelta(hours=1)
    routine = f"Start winding down at {routine_start.strftime('%H:%M')}"
    routine_label.config(text=routine)

root = tk.Tk()
root.title("Sleep Routine Advisor")

tk.Label(root, text="Bed Time (HH:MM):").grid(row=0, column=0)
bed_time_entry = tk.Entry(root)
bed_time_entry.grid(row=0, column=1)

tk.Label(root, text="Wake Time (HH:MM):").grid(row=1, column=0)
wake_time_entry = tk.Entry(root)
wake_time_entry.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate_sleep_time).grid(row=2, column=0, columnspan=2)

sleep_duration_label = tk.Label(root, text="")
sleep_duration_label.grid(row=3, column=0, columnspan=2)

routine_label = tk.Label(root, text="")
routine_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
