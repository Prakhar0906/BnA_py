import serial

device= serial.Serial('COM5',9600)

while True:
    if (device.inWaiting() > 0):
        data= device.readline()[:-2]
        data= data.decode()
        print(data)
        
