# Foster Ecklund
# Relectric Interior Team 

# ***********************************************************************
#                       CANHandler.py
# File Contains The Class Used to read and write from the CAN bus
# ***********************************************************************

#Library Imports
import queue
from random import randint
from time import sleep

#Import Global Variables form Globals
import Globals

# CanBus Handler Class
class CANHandler:
    def __init__(self) -> None:
        self.write_queue = queue.Queue()
        self.running = True

    def run(self):
        while self.running:
            if not self.write_queue.empty():
                message = self.write_queue.get()
                self.writeCanBus(message)

            self.readCanBus()    

            sleep(0.1)

    def stop(self):
        self.running = False     

    def readCanBus(self):       
        # Simulating reading from CAN bus
        new_value = randint(1,1000)  # Replace with actual CAN bus reading logic

        # Update global variable safely
        with Globals.data_lock:
            Globals.can_bus_value = new_value

    def writeCanBus(self, message):
        print("CAN Bus: " + message) # Replace with actual CAN bus writing logic

    def queueMessage(self,message):
        self.write_queue.put(message)