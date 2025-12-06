import tkinter as tk
from tkinter import Menu, END, Scrollbar, RIGHT, Y

# -----------------------------
# To-Do List GUI - Module 10.2
# Modified per assignment requirements
# -----------------------------

def add_task():
    task = entry.get()
    if task.strip():
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task(event):
    """Delete a task on RIGHT-click."""
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])

def exit_program():
    root.destroy()

# -----------------------------
# Window setup
# -----------------------------
root = tk.Tk()
root.title("LastName-ToDo")  # << CHANGE TO YOUR LAST NAME
root.geometry("400x450")

# -----------------------------
# Menu bar
# -----------------------------
menu_bar = Menu(root, background="#5A8DEE", foreground="white")   # complementary color 1
file_menu = Menu(menu_bar, tearoff=0, background="#FFAC41", foreground="black")  # complementary color 2
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# -----------------------------
# Instructions label
# -----------------------------
label = tk.Label(root, text="Right-click a task to delete it", font=("Arial", 12), pady=10)
label.pack()

# -----------------------------
# Listbox + Scrollbar
# -----------------------------
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = tk.Listbox(
    frame,
    width=40,
    height=12,
    yscrollcommand=scrollbar.set,
    font=("Arial", 12)
)

listbox.pack()

scrollbar.config(command=listbox.yview)

# -----------------------------
# Bind right-click delete
# -----------------------------
listbox.bind("<Button-3>", delete_task)   # RIGHT CLICK

# -----------------------------
# Entry + Add Button
# -----------------------------
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, padx=5)

add_button = tk.Button(entry_frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1)

# -----------------------------
# Run application
# -----------------------------
root.mainloop()
