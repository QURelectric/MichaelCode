# Foster Ecklund
# Relectric Interior Team 

# ***********************************************************************
#                       AppWindows.py
# File Contains The Classe for the Dashboard shown on the second display
# ***********************************************************************

# Library Imports
import tkinter as tk
from tkinter import ttk

#Import Global Variables from Globals
import Globals

# Dashboard Class
class DashboardWindowApp:
    def __init__(self, root, size) -> None:
        self.display = tk.Toplevel(root)
        self.display.title("Second Display")
        self.display.geometry(size)

        self.label = ttk.Label(self.display, text="CAN Bus Value: ")
        self.label.pack(pady=20)

        self.display.after(200, self.updateGUI)

    def updateGUI(self):
        with Globals.data_lock:
            value = Globals.can_bus_value

        # Update the label text
        if value is not None:
            self.label.config(text=f"CAN Bus Value: {value}")

        self.display.after(200, self.updateGUI)
