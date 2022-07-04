import serial

ser= serial.Serial('COM7', 9600, timeout= 1)

def Data():
    ser.write(b'1')
    data= ser.readline().decode('ascii')
    return data

while True:
    uInput= input("Retrive data?:")
    if uInput == '1':
        print(Data())
    else :
        der.write(b'0')
