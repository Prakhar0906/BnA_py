import serial
import time

serialcom= serial.Serial('COM5', 9600)
serialcom.timeout = 1

while True:
    i= input("Input(om/off):").strip()
    if i == 'done':
        print("Finished program")
        break
    serialcom.write(i.encode())
    time.sleep(0.5)
    print(serialcom.readline().decode('ascii'))

serialcom.close()
