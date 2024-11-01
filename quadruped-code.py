import tkinter as tk
from tkinter import ttk, messagebox
import json
import serial
#import opencv

class Servo:
    """Represents a servo motor in the GUI."""
    
    def __init__(self, parent, servo_id, name, x, y, min_val=0, max_val=180):
        """Initialize a servo control in the GUI at specific pixel coordinates."""
        pass

    def get_value(self):
        """Get the current value of the servo."""
        pass

    def set_value(self, value):
        """Set the value of the servo."""
        pass

class Leg:
    """Represents a leg of the quadruped, composed of two servos."""
    
    def __init__(self, parent, leg_id, base_x, base_y):
        """Initialize a leg with hip and ankle servos at specific positions."""
        pass


quadPositions = [0, 0, 0, 0, 0, 0, 0, 0]

class Quadruped:
    """Represents the entire quadruped robot."""
    
    def __init__(self, parent):
        """Initialize the quadruped with four legs."""
        pass

    def get_all_positions(self):
        """Get positions of all servos in the quadruped."""
        pass

    def set_all_positions(self, positions):
        """Set positions of all servos in the quadruped."""
        pass

class StateManager:
    """Manages saving and loading of robot states."""
    
    def __init__(self):
        pass

    def load_states(self, filename):
        # Opening JSON file
        with open(filename, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
            print("Loaded file")
        listLength = len(quadPositions)
        for item in range(listLength):
            quadPositions[item] = json_object[item]
        pass

    def save_states(self, filename):
        json_object = json.dumps(quadPositions, indent=8)
        with open(filename, "w") as outfile:
            outfile.write(json_object)
        pass

    def get_state(self, name):
        """Get a specific state by name."""
        pass

    def set_state(self, name, state):
        """Set a specific state by name."""
        pass

class SerialCommunicator:
    """Handles serial communication with the Pico."""
    
    def __init__(self, port='/dev/ttyACM0', baud_rate=115200):
        """Initialize the serial connection."""
        pass

    def send_command(self, command):
        """Send a command to the Pico."""
        pass

    def receive_data(self):
        """Receive data from the Pico."""
        pass


class QuadrupedGUI:
    """Main GUI class for controlling the quadruped robot."""

    def __init__(self, root):
        pass

    def update_pico(self):
        """Send updated positions to the Pico."""
        pass

    def create_gui(self):

        #Hip Servos
        slider0 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider0.pack()
        label0 = tk.Label(text="Hip servo 1")
        label0.pack()
        slider1 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider1.pack()
        label1 = tk.Label(text="Hip servo 2")
        label1.pack()
        slider2 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider2.pack()
        label2 = tk.Label(text="Hip servo 3")
        label2.pack()
        slider3 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider3.pack()
        label3 = tk.Label(text="Hip servo 4")
        label3.pack()

        #Ankle servos
        slider4 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider4.pack()
        label4 = tk.Label(text="Ankle servo 1")
        label4.pack()
        slider5 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider5.pack()
        label5 = tk.Label(text="Ankle servo 2")
        label5.pack()
        slider6 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider6.pack()
        label6 = tk.Label(text="Ankle servo 3")
        label6.pack()
        slider7 = tk.Scale(root, from_=0, to=42, orient=tk.HORIZONTAL)
        slider7.pack()
        label7 = tk.Label(text="Ankle servo 4")
        label7.pack()


        def set_position_values():
            quadPositions[0] = slider0.get()
            quadPositions[1] = slider1.get()
            quadPositions[2] = slider2.get()
            quadPositions[3] = slider3.get()
            quadPositions[4] = slider4.get()
            quadPositions[5] = slider5.get()
            quadPositions[6] = slider6.get()
            quadPositions[7] = slider7.get()
            for item in quadPositions:
                print(item)

        
        updateButton = tk.Button(text="Update positions", width=25, height=2, 
                                 command= lambda : set_position_values())
        updateButton.pack()
        saveButton = tk.Button(text="Save all positions", width=25, height=2,
                               command= lambda : QuadrupedGUI.save_state(root))
        saveButton.pack()
        loadButton = tk.Button(text="Load saved positions", width=25, height=2,
                               command= lambda : QuadrupedGUI.load_state(root, sliderList))
        loadButton.pack()

        sliderList = [slider0, slider1, slider2, slider3, slider4, slider5, slider6, slider7]
        return sliderList

    def save_state(self):
        StateManager.save_states(root, "quadSaveStates.json")
        pass

    def load_state(self, sliderList):
        StateManager.load_states(root, "quadSaveStates.json")
        listLength = len(quadPositions)
        for value in range(listLength):
            sliderList[value].set(quadPositions[value])
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = QuadrupedGUI(root)
    app.load_state(app.create_gui())
    root.mainloop()
