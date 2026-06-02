from tkinter import *
from tkinter import filedialog, messagebox
from datetime import datetime
import os

# Statistics Variables
total_keys = 0
letters = 0
numbers = 0
specials = 0

LOG_FILE = "keystroke_logs.txt"


# Log Keystrokes
def log_key(event):
    global total_keys, letters, numbers, specials

    key = event.keysym
    timestamp = datetime.now().strftime("%H:%M:%S")

    total_keys += 1

    if len(event.char) == 1:
        if event.char.isalpha():
            letters += 1
        elif event.char.isdigit():
            numbers += 1
        elif not event.char.isalnum():
            specials += 1

    entry = f"[{timestamp}] {key}\n"

    log_text.insert(END, entry)
    log_text.see(END)

    update_stats()


# Update Statistics
def update_stats():
    total_label.config(text=f"Total Keys: {total_keys}")
    letter_label.config(text=f"Letters: {letters}")
    number_label.config(text=f"Numbers: {numbers}")
    special_label.config(text=f"Special Chars: {specials}")


# Export Logs
def export_logs():
    content = log_text.get("1.0", END)

    if not content.strip():
        messagebox.showwarning(
            "Warning",
            "No logs available to export."
        )
        return

    with open(LOG_FILE, "w", encoding="utf-8") as file:
        file.write(content)

    messagebox.showinfo(
        "Success",
        f"Logs saved successfully as\n{LOG_FILE}"
    )


# Open Log File
def open_log_file():
    try:
        if os.path.exists(LOG_FILE):
            os.startfile(LOG_FILE)
        else:
            messagebox.showwarning(
                "File Not Found",
                "Please export logs first."
            )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


# Clear Logs
def clear_logs():
    global total_keys, letters, numbers, specials

    log_text.delete("1.0", END)

    total_keys = 0
    letters = 0
    numbers = 0
    specials = 0

    update_stats()

    messagebox.showinfo(
        "Success",
        "Logs cleared successfully!"
    )


# Main Window
root = Tk()
root.title("Advanced Keystroke Logger Demo")
root.geometry("1000x850")
root.configure(bg="#EAF4FC")


# Title
title = Label(
    root,
    text="⌨️ Advanced Keystroke Logger Demo",
    font=("Arial", 24, "bold"),
    bg="#EAF4FC",
    fg="#003366"
)
title.pack(pady=15)

subtitle = Label(
    root,
    text="Records only keys typed inside this application window",
    font=("Arial", 11),
    bg="#EAF4FC"
)
subtitle.pack()

# Typing Area
typing_frame = LabelFrame(
    root,
    text="Type Here",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)
typing_frame.pack(fill="x", padx=20, pady=10)

typing_box = Text(
    typing_frame,
    height=6,
    font=("Consolas", 12)
)
typing_box.pack(fill="x")

typing_box.bind("<Key>", log_key)

# Statistics Section
stats_frame = LabelFrame(
    root,
    text="Live Statistics",
    font=("Arial", 12, "bold")
)
stats_frame.pack(fill="x", padx=20, pady=10)

total_label = Label(
    stats_frame,
    text="Total Keys: 0",
    font=("Arial", 12, "bold")
)
total_label.grid(row=0, column=0, padx=20, pady=10)

letter_label = Label(
    stats_frame,
    text="Letters: 0",
    font=("Arial", 12, "bold")
)
letter_label.grid(row=0, column=1, padx=20)

number_label = Label(
    stats_frame,
    text="Numbers: 0",
    font=("Arial", 12, "bold")
)
number_label.grid(row=0, column=2, padx=20)

special_label = Label(
    stats_frame,
    text="Special Chars: 0",
    font=("Arial", 12, "bold")
)
special_label.grid(row=0, column=3, padx=20)

button_frame = Frame(root, bg="#EAF4FC")
button_frame.pack(pady=15)

export_btn = Button(
    button_frame,
    text="📄 Export Logs",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    padx=15,
    command=export_logs
)
export_btn.grid(row=0, column=0, padx=10)

clear_btn = Button(
    button_frame,
    text="🗑 Clear Logs",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    padx=15,
    command=clear_logs
)
clear_btn.grid(row=0, column=1, padx=10)

open_btn = Button(
    button_frame,
    text="📂 Open Log File",
    font=("Arial", 12, "bold"),
    bg="#0066CC",
    fg="white",
    padx=15,
    command=open_log_file
)
open_btn.grid(row=0, column=2, padx=10)

exit_btn = Button(
    button_frame,
    text="❌ Exit",
    font=("Arial", 12, "bold"),
    bg="#444444",
    fg="white",
    padx=15,
    command=root.destroy
)
# Live Logs Section
log_frame = LabelFrame(
    root,
    text="Live Keystroke Logs",
    font=("Arial", 12, "bold")
)
log_frame.pack(fill="both", expand=True, padx=20, pady=10)

scrollbar = Scrollbar(log_frame)
scrollbar.pack(side=RIGHT, fill=Y)

log_text = Text(
    log_frame,
    font=("Consolas", 11),
    yscrollcommand=scrollbar.set
)
log_text.pack(fill="both", expand=True)

scrollbar.config(command=log_text.yview)



exit_btn.grid(row=0, column=3, padx=10)

root.mainloop()