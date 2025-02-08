# Foster Ecklund
# Relectric Interior Team

# *******************************************
#                   MainApp.py
#       This is the main file for the GUI
# *******************************************

# Import Libraries
import threading

# Import Classes
from DashboardWindow import DashboardWindowApp
from HomeWindow import HomeWindow

# Import Globals for Global Variables
import Globals

if __name__ == "__main__":
    # Initialize HomeWindow Object
    home_window = HomeWindow(Globals.root, Globals.mainWindowSize)

    # Initialize Secondary window
    dashboard_window = DashboardWindowApp(Globals.root, Globals.secondWindowSize)

    # Create and start the CAN bus reading thread
    CAN_thread = threading.Thread(target=Globals.Handler.run, daemon=True)
    CAN_thread.start()

    # Run the main application loop
    Globals.root.mainloop()
