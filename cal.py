import tkinter as tk
import math
from statistics import mean, median

cal = tk.Tk()
cal.title("CALCULATOR")
cal.geometry("350x450")

entry = tk.Entry(cal, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")


BG_COLOR = "#000000"      
BTN_COLOR = "#210B53"      
BTN_TEXT = "#F4F3FB"       
ENTRY_BG = "#e2f7f3"      
ENTRY_FG = "#000000"       

cal.configure(bg=BG_COLOR)

entry = tk.Entry(
    cal, font=("Arial", 20), borderwidth=5, relief="ridge",
    justify="right", bg=ENTRY_BG, fg=ENTRY_FG
)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")
def add_to_entry(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    if len(current) > 0:
        entry.delete(len(current) - 1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def scientific_function(func):
    try:
        exp = entry.get()
        if func == "mean":
            nums = list(map(float, exp.split(",")))
            result = mean(nums)
        elif func == "median":
            nums = list(map(float, exp.split(",")))
            result = median(nums)
        else:
            value = float(exp)
            if func == "sin":
                result = math.sin(math.radians(value))
            elif func == "cos":
                result = math.cos(math.radians(value))
            elif func == "tan":
                result = math.tan(math.radians(value))
            elif func == "log":
                result = math.log10(value)
            elif func == "ln":
                result = math.log(value)
            elif func == "sqrt":
                result = math.sqrt(value)
            elif func == "pi":
                result = math.pi
            elif func == "e":
                result = math.e
            elif func == "cube":
                result = value**3
            elif func == "square":
                result = value*value

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(
            cal, text=text, width=5, height=2, font=("Arial",15),
            bg=BTN_COLOR, fg=BTN_TEXT, activebackground=BTN_COLOR,
            command=calculate
        ).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(
            cal, text=text, width=5, height=2, font=("Arial", 15),
            bg=BTN_COLOR, fg=BTN_TEXT, activebackground=BTN_COLOR,
            command=lambda x=text: add_to_entry(x)
        ).grid(row=row, column=col, sticky="nsew")

tk.Button(
    cal, text="C", width=5, height=2, font=("Arial", 15),
    bg=BTN_COLOR, fg=BTN_TEXT, activebackground=BTN_COLOR,
    command=clear_entry
).grid(row=5, column=0, columnspan=2, sticky="nsew")

tk.Button(
    cal, text="←", width=5, height=2, font=("Arial", 15),
    bg=BTN_COLOR, fg=BTN_TEXT, activebackground=BTN_COLOR,
    command=backspace
).grid(row=5, column=2, columnspan=2, sticky="nsew")

sci_frame = tk.Frame(cal)

sci_buttons = [
    ("sin", 0, 0), ("cos", 0, 1), ("tan", 0, 2),
    ("log", 1, 0), ("ln", 1, 1), ("sqrt", 1, 2),
    ("pi", 2, 0), ("e", 2, 1), ("root",2,2),
    ("mean", 3, 0), ("median", 3, 1), ("cube",3,2)
]

for (text, row, col) in sci_buttons:
    tk.Button(sci_frame, text=text, width=7, height=2, font=("Arial", 12),
              command=lambda x=text: scientific_function(x)).grid(row=row, column=col, padx=5, pady=5)

sci_visible = False

def toggle_scientific():
    global sci_visible
    if sci_visible:
        sci_frame.grid_forget()
        toggle_btn.config(text="More Functions")
        cal.geometry("350x600")
    else:
        sci_frame.grid(row=6, column=0, columnspan=4)
        toggle_btn.config(text="Hide")
        cal.geometry("350x750")

    sci_visible = not sci_visible

toggle_btn = tk.Button(cal, text="More Functions", font=("Arial", 15),
                       command=toggle_scientific)
toggle_btn.grid(row=7, column=0, columnspan=4, sticky="nsew", pady=10)

cal.mainloop()
