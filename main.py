from tkinter import ttk
from tkinter import *
import sqlite3
from models import Principal

if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300")
    app = Principal(root)
    root.mainloop()