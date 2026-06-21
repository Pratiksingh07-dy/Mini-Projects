import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Display
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            tk.Button(
                frame,
                text=btn,
                font=("Arial", 18),
                command=calculate
            ).pack(side="left", expand=True, fill="both")
        else:
            tk.Button(
                frame,
                text=btn,
                font=("Arial", 18),
                command=lambda x=btn: click(x)
            ).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()