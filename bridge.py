import serial
import requests

ser = serial.Serial('COM2', 9600, timeout=1)
print("Listening to Proteus on COM2...")

while True:
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    if line.startswith("GET /update"):
        url = "https://api.thingspeak.com" + line.replace("GET ", "")
        print("Sending:", url)
        try:
            response = requests.get(url)
            print("ThingSpeak Entry ID:", response.text)
        except Exception as e:
            print("Error:", e)
