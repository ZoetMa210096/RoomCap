
from flask import Flask
import serial
import logging
import threading
import time

personCount = 0 

def poll_arduino():

    global personCount
    print("Poll Arduino")
    
    arduino = serial.Serial('COM4', 9600)
    lastValue = False

    while True:
        data = arduino.readline().decode('utf-8').strip()

        #serial.flushInput()
        if data=="no":
            lastValue = data
            pass
        if data=="yes" and lastValue!=data:
            personCount = personCount + 1
            lastValue = data
        print(personCount)

arduino_thread = threading.Thread(target=poll_arduino, daemon=True)
arduino_thread.start()

app = Flask(__name__)

@app.route("/")
def hello_world():

    return "<h1>This is our LightSensor Project!</h1>" + " " + str(personCount)
    
    