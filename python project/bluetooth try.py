import serial
import time

print("Start")

device= serial.Serial('COM7', 9600)

if (device.inWaiting() > 0) :
    device.send("a".encode())
