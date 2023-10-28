
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import serial
import logging
import threading
import time

personCount = 0 

def poll_arduino():

    global personCount
    print("Poll Arduino")
    
    arduino = serial.Serial('COM5', 9600)
    lastValue = False

    while True:
        data = arduino.readline().decode('utf-8').strip()

        #serial.flushInput()
        if data=="Rausgehen":
            personCount = personCount - 1
            pass
        if data=="Reingehen":
            personCount = personCount + 1
            lastValue = data
        print(personCount)

arduino_thread = threading.Thread(target=poll_arduino, daemon=True)
arduino_thread.start()

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
CORS(app, support_credentials=True)

@app.route("/")
def index():
    return render_template('index.html')

    if __name__=='__main__':
        app.run(debug = True)

@app.route("/personCountFunction")
@cross_origin(supports_credentials=True)
def personCountFunction():
    return str(personCount)
