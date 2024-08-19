import adafruit_dht
import board
from gpiozero import DistanceSensor
import time
import numpy as np
import matplotlib.pyplot as plt

#Sensors Setup
dht_device = adafruit_dht.DHT11(board.D17)
ultrasonic_sensor = DistanceSensor(echo=18, trigger=17)

y1 = []
y2 = []
x = []

#open a log file
flog = open("Readings.log", 'a')

for i in range(5):
    try:
        # Read temperature and humidity from the sensor
        temperature = dht_device.temperature
        distance = ultrasonic_sensor.distance
        y1.append(temperature) 
        y2.append(distance)
        x.append(i+1)

        #store in the log file
        flog.write(f"Temperature: {temperature}\u00b0C\n")
        flog.write(f"Distance: {distance}%\n")

        # Print the results
        print(f"Temperature: {temperature}\u00b0C")
        print(f"Distance: {distance}%")
    
    except RuntimeError as error:
        # Handle runtime errors (such as timeouts)
        print(f"Error reading sensor data: {error.args[0]}")
    
    # Wait for a short period before reading again
    time.sleep(2)

flog.close()

plt.plot(x,y1, c='r', label = 'Temperature', marker = 'o')
plt.plot(x,y2, c ='b', label = 'Distance', marker = '*')

plt.legend()
plt.title('Temperature and Distance')
plt.xlabel('time (s)')
plt.ylabel('\u00b0C / %')

plt.show()