# Foster Ecklund & Michael Whitwam
# Relectric Interior Team

# *******************************************
#              HomeWindow.py
#       This is the main file for the GUI
# *******************************************

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from SubWindows import MusicWindow, NavagationWindow, ControlWindow

class HomeWindow:
    def __init__(self, root, size):
        #Initialize instance variables
        self.window = root  #Use the provided root window
        self.window.title("HomeWindow") #Window Name
        self.window.geometry(size)  #Use the provided size
        
        self.lock = False #Variable for the lock function
        self.temperature = 21 #Variable for the tempature
        
        #BACKGROUND IMAGE
        background_image = Image.open("Orion.png").resize((800, 480), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(background_image)
        bg_label = tk.Label(self.window, image=self.bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        
        #BLACK BAR AT THE BOTTOM OF SCREEN
        black_bar = tk.Label(self.window, bg="black", height=3)
        black_bar.place(relwidth=1, relheight=0.10, rely=0.90)

        #SPOTIFY BUTTON
        imageSpotify = Image.open("spotifyLogo.png").resize((30, 30), Image.Resampling.LANCZOS)
        self.image_Spotify = ImageTk.PhotoImage(imageSpotify)
        buttonSpotify = tk.Label(self.window, image=self.image_Spotify, bd=0)
        buttonSpotify.bind("<Button-1>", lambda e: MusicWindow(self.window, size))
        buttonSpotify.place(x=325, y=440)

        #VOLUME SLIDER
        style = ttk.Style()
        style.configure("TScale", troughcolor="#000000", sliderlength=20, background="#555555")
        slider = ttk.Scale(self.window, from_=0, to=100, orient="horizontal", length=300, style="TScale")
        slider.place(x=460, y=454)

        #VOLUME "+" AND "-"
        labelVolumePlus = tk.Label(self.window, text="+", font=("Calibri", 35), fg="white", bg="black")
        labelVolumePlus.place(x=765, y=438)
        labelVolumeMinus = tk.Label(self.window, text="-", font=("Calibri", 35), fg="white", bg="black")
        labelVolumeMinus.place(x=434, y=438)
        labelVolume = tk.Label(self.window, text="VOLUME", font=("Calibri", 11), fg="white", bg="black")
        labelVolume.place(x=585, y=432)

        #TEMPATURE LABEL
        self.temperature = 21  # Initial temperature
        
        self.labelTemperature = tk.Label(self.window, text=str(self.temperature), font=("Calibri", 30), fg="white", bg="black")
        self.labelTemperature.place(x=98, y=432)

        #TEMPATURE DOWN ARROW
        imageLeftArrow = Image.open("LeftArrow.png").resize((10, 10), Image.Resampling.LANCZOS)
        self.TKLeftArrow = ImageTk.PhotoImage(imageLeftArrow)
        buttonLeftArrow = tk.Label(self.window, image=self.TKLeftArrow, bd=0)
        buttonLeftArrow.bind("<Button-1>", lambda e: self.temperatureUpdate(increase=False))
        buttonLeftArrow.place(x=76, y=450)

        #TEMPATURE UP ARROW
        imageRightArrow = Image.open("RightArrow.png").resize((10, 10), Image.Resampling.LANCZOS)
        self.TKRightArrow = ImageTk.PhotoImage(imageRightArrow)
        buttonRightArrow = tk.Label(self.window, image=self.TKRightArrow, bd=0)
        buttonRightArrow.bind("<Button-1>", lambda e: self.temperatureUpdate(increase=True))
        buttonRightArrow.place(x=150, y=450)

        #CAMERA BUTTON
        cameraLogo = Image.open("CameraLogo.png").resize((30, 30), Image.Resampling.LANCZOS)
        self.TKcameraLogo = ImageTk.PhotoImage(cameraLogo)
        buttonCamera = tk.Label(self.window, image=self.TKcameraLogo, bd=0)
        buttonCamera.bind("<Button-1>", lambda e: self.clickCamera())
        buttonCamera.place(x=375, y=440)

        #SETTINGS BUTTON
        settingLogo = Image.open("Setting.png").resize((30, 30), Image.Resampling.LANCZOS)
        self.TKsettingLogo = ImageTk.PhotoImage(settingLogo)
        buttonSetting = tk.Label(self.window, image=self.TKsettingLogo, bd=0)
        buttonSetting.bind("<Button-1>", lambda e: NavagationWindow(self.window, size))
        buttonSetting.place(x=20, y=440)

        #LOCK BUTTON
        lockLogo = Image.open("Lock.png").resize((140, 140), Image.Resampling.LANCZOS).convert("RGBA")
        self.TKLockLogo = ImageTk.PhotoImage(lockLogo)
        unlockLogo = Image.open("Unlock.png").resize((140, 140), Image.Resampling.LANCZOS).convert("RGBA")
        self.TKUnlockLogo = ImageTk.PhotoImage(unlockLogo)
        buttonLock = tk.Label(self.window, image=self.TKLockLogo, bd=0)
        buttonLock.bind("<Button-1>", lambda e: self.clickLock(buttonLock))
        buttonLock.place(x=40, y=40)

        #START ENGINE BUTTON
        startLogo = Image.open("Start.png").resize((140, 140), Image.Resampling.LANCZOS).convert("RGBA")
        self.TKStartLogo = ImageTk.PhotoImage(startLogo)
        startButton = tk.Button(self.window, image=self.TKStartLogo, command=lambda: ControlWindow(self.window, size))
        startButton.place(x=40, y=250)

        #MAP IMAGE
        mapImage = Image.open("map.png").resize((550, 380), Image.Resampling.LANCZOS)
        self.TKMap = ImageTk.PhotoImage(mapImage)
        labelMap = tk.Label(self.window, image=self.TKMap)
        labelMap.place(x=220, y=27)

        #RUN WINDOW MAIN LOOP
        self.window.mainloop()

    
    #Function for camera click
    def clickCamera(self):
        print("Camera was clicked!")

    #Function for lock button
    def clickLock(self, buttonLock):
        if self.lock:
            buttonLock.config(image=self.TKLockLogo) #Switch Image
            print("Door locked")
            self.lock = False
        else:
            buttonLock.config(image=self.TKUnlockLogo) #Switch Image
            print("Door unlocked")
            self.lock = True

    def tempatureUpdate(self, increase=True):
     if increase:
        if self.temperature < 30:  # Allow increase only if below 30
            self.temperature += 1
            self.labelTemperature.config(text=str(self.temperature), font=("Calibri", 30))  # Update label
            self.labelTemperature.place(x=98, y=432)  # Positioning
        else:
            self.labelTemperature.config(text="MAX", font=("Calibri", 20))  # Update label for max
            self.labelTemperature.place(x=95, y=439)  # Positioning for MAX
     else:
        if self.temperature > 15:  # Allow decrease only if above 15
            self.temperature -= 1
            self.labelTemperature.config(text=str(self.temperature), font=("Calibri", 30))  # Update label
            self.labelTemperature.place(x=98, y=432)  # Positioning
        else:
            self.labelTemperature.config(text="MIN", font=("Calibri", 20))  # Update label for min
            self.labelTemperature.place(x=98, y=439)  # Positioning for MIN


if __name__ == "__main__":
    root = tk.Tk()
    app = HomeWindow(root, "800x480+800+0")
    root.mainloop()
