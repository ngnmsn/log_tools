import tkinter as tk
from tkinter import ttk

class tkwindow:
    def __init__(self, title):
        self.title = title
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry('1000x700')
        # root.mainloop() 
    