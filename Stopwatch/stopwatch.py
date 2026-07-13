import tkinter as tk

running = False
elapsed_time = 0


def update_timer():
    global elapsed_time
    if running:
        elapsed_time += 1

        minutes = elapsed_time // 60
        seconds = elapsed_time % 60

        timer_label.config(text=f"{minutes:02}:{seconds:02}")

        root.after(1000, update_timer)


def start():
    global running
    if not running:
        running = True
        update_timer()


def stop():
    global running
    running = False


def reset():
    global running, elapsed_time
    running = False
    elapsed_time = 0
    timer_label.config(text="00:00")


# ---------------- Window ---------------- #

root = tk.Tk()
root.title("Stopwatch")
root.geometry("350x250")
root.resizable(False, False)

timer_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 40, "bold")
)
timer_label.pack(pady=30)

button_frame = tk.Frame(root)
button_frame.pack()

start_btn = tk.Button(
    button_frame,
    text="Start",
    font=("Arial", 14),
    width=8,
    command=start
)
start_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(
    button_frame,
    text="Stop",
    font=("Arial", 14),
    width=8,
    command=stop
)
stop_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(
    button_frame,
    text="Reset",
    font=("Arial", 14),
    width=8,
    command=reset
)
reset_btn.grid(row=0, column=2, padx=5)

root.mainloop()