from machine import Pin, PWM
import sys
import time

servoAnkle1 = PWM(Pin(0))
servoHip1 = PWM(Pin(1))
servoAnkle2 = PWM(Pin(2))
servoHip2 = PWM(Pin(3))
servoHip3 = PWM(Pin(12))
servoAnkle3 = PWM(Pin(13))
servoHip4 = PWM(Pin(14))
servoAnkle4 = PWM(Pin(15))


servoList = [servoHip1, servoHip2, servoHip3, servoHip4, servoAnkle1, servoAnkle2, servoAnkle3, servoAnkle4]

def degrees_to_duty(degrees):
    # Assuming servos have a range of 1ms to 2ms pulse width
    min_pulse_width = 1000  # Minimum pulse width in microseconds
    max_pulse_width = 2000  # Maximum pulse width in microseconds
    pulse_width = min_pulse_width + (degrees / 180.0) * (max_pulse_width - min_pulse_width)
    # Convert microseconds to duty cycle for 50Hz (20ms period)
    return int((pulse_width / 20000.0) * 65535)

def set_value(value, servo, wait): #Moves servo to new position
    servo.freq(50)
    servo.duty_u16(degrees_to_duty(value))
    print(f"{servo} moved to {value} degrees")
    time.sleep(wait)
    servo.duty_u16(0)
     
def start_wave(): #Process for the Pico to wave
    set_value(270, servoAnkle1, 0.5)
    set_value(200, servoHip1, 0.2)
    set_value(100, servoHip1, 0.2)
    set_value(200, servoHip1, 0.2)
    set_value(100, servoHip1, 0.5)
    set_value(0, servoAnkle1, 0.5)

def receive_data(): #Receives data from GUI
    v = sys.stdin.readline()
    if v.strip() == "wave":
        start_wave()
    else:
        v = v.split(",")
        for item in range(len(servoList)):
            set_value(float(v[item]), servoList[item], 0.5)
        
while True:# Main Program Loop
    receive_data()