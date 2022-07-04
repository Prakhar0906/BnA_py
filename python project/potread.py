import serial

arduino= serial.Serial('COM5',9600)
arduino.timeout=1

while True:
        val= arduino.readline()
        value= val.decode()
        print(value);
