import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def show_shrimp():
    # New window with shrimp image
    shrimp_window = tk.Toplevel(root)
    shrimp_window.title("You're a shrimp!")

    # Load and display the image
    img = Image.open("HAHA.jpeg")  # replace with your image file name
    img = img.resize((2000, 2000))
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(shrimp_window, image=img)
    img_label.image = img  # keep a reference
    img_label.pack()

    # Play the sound using afplay after a short delay
    shrimp_window.after(500, lambda: subprocess.run(["afplay", "LAUGH.mp3"]))  # 500ms delay

def check_if_shrimp():
    answer = messagebox.askquestion("Are you a shrimp?", "Are you a shrimp?")
    if answer == "yes":
        show_shrimp()

# Main window setup
root = tk.Tk()
root.title("Shrimp Detector")
root.geometry("300x100")

# Button to trigger shrimp check
btn = tk.Button(root, text="START", command=check_if_shrimp)
btn.pack(pady=20)

root.mainloop()
