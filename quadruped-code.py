import tkinter as tk
from tkinter import ttk, messagebox
import json
import serial


quadPositions = [0, 0, 0, 0, 0, 0, 0, 0]

class StateManager:
    
    stateName = ""

    def loadStates(self, filename): #Loads positions from file
        # Opening JSON file
        try:
            with open(filename, 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)
                print("Loaded file")
            listLength = len(quadPositions)
            for item in range(listLength):
                quadPositions[item] = json_object[item]
            pass
        except:
            print("Loading error, continuing as normal")

    def saveStates(self, filename): #Writes current positions list to file
        json_object = json.dumps(quadPositions, indent=8)
        with open(filename, "w") as outfile:
            outfile.write(json_object)
        print("Saved all positions to file")
        
####################################
####################################
####################################
####################################

class SerialCommunicator:
    
    """Handles serial communication with the Pico."""
        
    def send_command(self, command, s): #Sends instructions to Pico
        if command == "numbers":
            numbers = f"{quadPositions[0]},{quadPositions[1]},{quadPositions[2]},{quadPositions[3]},{quadPositions[4]},{quadPositions[5]},{quadPositions[6]},{quadPositions[7]}\n"
            s.write(numbers.encode())
        elif command == "wave":
            s.write("wave\n".encode())
    
####################################
####################################
####################################
####################################

class QuadrupedGUI:
    """Main GUI class for controlling the quadruped robot."""
    
    def update_pico(self, command): #Starts serial communication without major error
        s = serial.Serial("COM8", 115200)
        SerialCommunicator.send_command(root, command, s)

    def create_gui(self): #Creates main GUI

        #Hip Servos
        slider0 = tk.Scale(root, from_=0, to=200, orient=tk.HORIZONTAL)
        slider0.pack()
        label0 = tk.Label(text="Hip servo 1")
        label0.pack()
        slider1 = tk.Scale(root, from_=90, to=-50, orient=tk.HORIZONTAL)
        slider1.pack()
        label1 = tk.Label(text="Hip servo 2")
        label1.pack()
        slider2 = tk.Scale(root, from_=0, to=-100, orient=tk.HORIZONTAL)
        slider2.pack()
        label2 = tk.Label(text="Hip servo 3")
        label2.pack()
        slider3 = tk.Scale(root, from_=0, to=270, orient=tk.HORIZONTAL)
        slider3.pack()
        label3 = tk.Label(text="Hip servo 4")
        label3.pack()

        #Ankle servos
        slider4 = tk.Scale(root, from_=200, to=0, orient=tk.HORIZONTAL)
        slider4.pack()
        label4 = tk.Label(text="Ankle servo 1")
        label4.pack()
        slider5 = tk.Scale(root, from_=-100, to=270, orient=tk.HORIZONTAL)
        slider5.pack()
        label5 = tk.Label(text="Ankle servo 2")
        label5.pack()
        slider6 = tk.Scale(root, from_=270, to=-100, orient=tk.HORIZONTAL)
        slider6.pack()
        label6 = tk.Label(text="Ankle servo 3")
        label6.pack()
        slider7 = tk.Scale(root, from_=-100, to=275, orient=tk.HORIZONTAL)
        slider7.pack()
        label7 = tk.Label(text="Ankle servo 4")
        label7.pack()


        def set_position_values(): #Updates servo position list
            quadPositions[0] = slider0.get()
            quadPositions[1] = slider1.get()
            quadPositions[2] = slider2.get()
            quadPositions[3] = slider3.get()
            quadPositions[4] = slider4.get()
            quadPositions[5] = slider5.get()
            quadPositions[6] = slider6.get()
            quadPositions[7] = slider7.get()
            QuadrupedGUI.update_pico(root, "numbers")

        
        waveButton = tk.Button(text="Make robot wave", width=25, height=2, command= lambda: QuadrupedGUI.update_pico(root, "wave"))
        waveButton.pack(side=tk.RIGHT)
        updateButton = tk.Button(text="Update positions", width=25, height=2, 
                                 command= lambda : set_position_values())
        updateButton.pack(side=tk.LEFT)
        saveButton = tk.Button(text="Save all positions", width=25, height=2,
                               command= lambda : QuadrupedGUI.saveState(root, fileNameEntry.get()))
        saveButton.pack(side=tk.LEFT)
        loadButton = tk.Button(text="Load saved positions", width=25, height=2,
                               command= lambda : QuadrupedGUI.loadState(root, sliderList, fileNameEntry.get()))
        loadButton.pack(side=tk.RIGHT)
        fileNameEntry = tk.Entry(text="Enter file name", width=25)
        fileNameEntry.pack(side=tk.RIGHT)

        sliderList = [slider0, slider1, slider2, slider3, slider4, slider5, slider6, slider7]
        return sliderList

    def saveState(self, filename):
        StateManager.saveStates(root, filename + ".json")
        pass

    def loadState(self, sliderList, filename):
        StateManager.loadStates(root, filename + ".json")
        listLength = len(quadPositions)
        for value in range(listLength):
            sliderList[value].set(quadPositions[value])
        pass
    

####################################
####################################
####################################
####################################

if __name__ == "__main__": #Main Program Process
    root = tk.Tk()
    app = QuadrupedGUI()
    app.loadState(app.create_gui(), "standing")
    root.geometry("800x800")
    root.mainloop()
