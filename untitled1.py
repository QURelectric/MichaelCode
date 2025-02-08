import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.geometry("200x200")  # Set window size to 200x200
window.configure(bg="blue")  # Set the background color to blue

# Load and process the image
start = Image.open("Start.png").convert("RGBA")  # Open image with alpha channel
start = start.resize((90, 90), Image.Resampling.LANCZOS)  # Resize image to fit button
TKStart = ImageTk.PhotoImage(start)  # Convert the image to tkinter format

# Create and display the label with the image
label = tk.Label(window, image=TKStart, bg="blue")  # Set the label background to match the window
label.pack(expand=True)  # Center the image in the window

# Run the window's main loop
window.mainloop()
