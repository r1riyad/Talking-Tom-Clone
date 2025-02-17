import tkinter as tk
from tkinter import messagebox
import threading
from recorder import record_audio
from modifier import modify_audio
from player import play_audio

def start_recording():
    threading.Thread(target=record_audio).start()
    messagebox.showinfo("Info", "Recording started. Speak now!")

def start_modifying():
    modify_audio()
    messagebox.showinfo("Info", "Audio modified successfully!")

def start_playing():
    threading.Thread(target=play_audio).start()

def start_gui():
    root = tk.Tk()
    root.title("Talking Tom Clone")
    root.geometry("300x200")

    tk.Label(root, text="Talking Tom Clone", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Record", command=start_recording).pack(pady=5)
    tk.Button(root, text="Modify Voice", command=start_modifying).pack(pady=5)
    tk.Button(root, text="Play Modified Voice", command=start_playing).pack(pady=5)

    root.mainloop()
