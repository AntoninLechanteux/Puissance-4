import tkinter as tk
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
print(width)
print(height)

root=tk.Tk()
root.geometry("720x480")
root.attributes("-fullscreen", True)
root.config(bg="#3394ff")
root.bind("<Escape>", lambda event: root.destroy()) 

