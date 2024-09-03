#!/usr/local/bin/python
import RPi.GPIO as GPIO
from gpiozero import LED
import time


led_pins = [17, 18, 27, 22, 23, 24]
ir_sensors = [4, 17, 27]
ldr_pin = 4  

for sensor in ir_sensors:
    GPIO.setup(sensor, GPIO.IN)

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def rc_time (pin_to_circuit):
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)

    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

def is_night():
  ldr_value = rc_time(ldr_pin)
  if ldr_value > 2500:
    return False
  else:
    return True
        
def control_leds(sensor_index):
    if is_night():
        if 0 <= sensor_index < len(led_pins) // 2:
            GPIO.output(led_pins[sensor_index * 2], GPIO.HIGH)
            GPIO.output(led_pins[sensor_index * 2 + 1], GPIO.HIGH)
    else:
        for pin in led_pins:
            GPIO.output(pin, GPIO.LOW)

try:
    while True:
        for i, pin in enumerate(ir_sensors):
            if GPIO.input(pin) == GPIO.HIGH:
                control_leds(i)
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()