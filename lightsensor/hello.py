from flask import Flask
import serial

app = Flask(__name__)

arduino = serial.Serial('COM4', 9600, timeout=1)

@app.route("/")
def hello_world():

  
    data = arduino.readline().decode('utf-8').strip()

    print(data)

    return "<h1>This is our LightSensor Project!</h1>" + " " + data
    
    