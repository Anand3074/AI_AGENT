import tkinter as tk
from tkinter import ttk
import subprocess

def calculate():
    expression = expression_entry.get()
    if not expression:
        result_label.config(text="Please enter an expression", foreground="#e74c3c")
        return
    
    try:
        result = subprocess.check_output(["python3", "calculator.py", expression]).decode("utf-8").strip()
        result_label.config(text=result, foreground="#27ae60")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", foreground="#e74c3c")

def send_instruction():
    instruction = instruction_entry.get()
    if instruction:
        print(f"You said: {instruction}")
        instruction_entry.delete(0, tk.END)
        feedback_label.config(text="✓ Instruction sent!", foreground="#27ae60")
        window.after(2000, lambda: feedback_label.config(text=""))
    else:
        feedback_label.config(text="Please enter an instruction", foreground="#e74c3c")
        window.after(2000, lambda: feedback_label.config(text=""))

def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(foreground="#2c3e50")

def on_focusout(event, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(foreground="#95a5a6")

# Create main window
window = tk.Tk()
window.title("Smart Calculator")
window.geometry("500x600")
window.configure(bg="#ecf0f1")
window.resizable(False, False)

# Header
header_frame = tk.Frame(window, bg="#3498db", height=80)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

title_label = tk.Label(
    header_frame, 
    text="Smart Calculator", 
    font=("Segoe UI", 24, "bold"),
    bg="#3498db",
    fg="white"
)
title_label.pack(pady=20)

# Main container
main_container = tk.Frame(window, bg="#ecf0f1")
main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Calculator Section
calc_frame = tk.Frame(main_container, bg="white", relief=tk.RAISED, bd=2)
calc_frame.pack(fill=tk.X, pady=(0, 20))

calc_header = tk.Label(
    calc_frame,
    text="🔢 Calculator",
    font=("Segoe UI", 16, "bold"),
    bg="white",
    fg="#2c3e50",
    anchor="w"
)
calc_header.pack(fill=tk.X, padx=20, pady=(15, 10))

expression_entry = tk.Entry(
    calc_frame,
    font=("Segoe UI", 14),
    bg="#ecf0f1",
    fg="#95a5a6",
    relief=tk.FLAT,
    borderwidth=2
)
expression_entry.insert(0, "Enter expression (e.g., 2+2)")
expression_entry.bind("<FocusIn>", lambda e: on_entry_click(e, expression_entry, "Enter expression (e.g., 2+2)"))
expression_entry.bind("<FocusOut>", lambda e: on_focusout(e, expression_entry, "Enter expression (e.g., 2+2)"))
expression_entry.pack(fill=tk.X, padx=20, pady=10, ipady=8)

calculate_button = tk.Button(
    calc_frame,
    text="Calculate",
    font=("Segoe UI", 12, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=calculate
)
calculate_button.pack(pady=10, ipadx=40, ipady=8)

result_frame = tk.Frame(calc_frame, bg="#ecf0f1", relief=tk.FLAT)
result_frame.pack(fill=tk.X, padx=20, pady=(10, 20))

result_title = tk.Label(
    result_frame,
    text="Result:",
    font=("Segoe UI", 11, "bold"),
    bg="#ecf0f1",
    fg="#7f8c8d"
)
result_title.pack(anchor="w", padx=10, pady=(10, 5))

result_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 16, "bold"),
    bg="#ecf0f1",
    fg="#27ae60",
    anchor="w"
)
result_label.pack(anchor="w", padx=10, pady=(0, 10))

# Interaction Section
interaction_frame = tk.Frame(main_container, bg="white", relief=tk.RAISED, bd=2)
interaction_frame.pack(fill=tk.X)

interaction_header = tk.Label(
    interaction_frame,
    text="💬 Instructions",
    font=("Segoe UI", 16, "bold"),
    bg="white",
    fg="#2c3e50",
    anchor="w"
)
interaction_header.pack(fill=tk.X, padx=20, pady=(15, 10))

instruction_entry = tk.Entry(
    interaction_frame,
    font=("Segoe UI", 14),
    bg="#ecf0f1",
    fg="#95a5a6",
    relief=tk.FLAT,
    borderwidth=2
)
instruction_entry.insert(0, "Type your instruction here...")
instruction_entry.bind("<FocusIn>", lambda e: on_entry_click(e, instruction_entry, "Type your instruction here..."))
instruction_entry.bind("<FocusOut>", lambda e: on_focusout(e, instruction_entry, "Type your instruction here..."))
instruction_entry.pack(fill=tk.X, padx=20, pady=10, ipady=8)

instruction_button = tk.Button(
    interaction_frame,
    text="Send Instruction",
    font=("Segoe UI", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=send_instruction
)
instruction_button.pack(pady=10, ipadx=30, ipady=8)

feedback_label = tk.Label(
    interaction_frame,
    text="",
    font=("Segoe UI", 10, "italic"),
    bg="white",
    fg="#27ae60"
)
feedback_label.pack(pady=(5, 20))

# Footer
footer = tk.Label(
    window,
    text="Press Enter to submit • Modern UI Design",
    font=("Segoe UI", 9),
    bg="#ecf0f1",
    fg="#95a5a6"
)
footer.pack(side=tk.BOTTOM, pady=10)

# Bind Enter key
expression_entry.bind("<Return>", lambda e: calculate())
instruction_entry.bind("<Return>", lambda e: send_instruction())

window.mainloop()