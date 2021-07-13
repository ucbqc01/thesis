import serial
import time
from serial import Serial
import csv
arduino_port = "/dev/cu.usbmodem14201" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="temperature-data.csv" #name of the CSV file generated
ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
#file = open(fileName, "a")
print("Created file")

samples = 1 #how many samples to collect
print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
while line <= samples:
    # incoming = ser.read(9999)
    # if len(incoming) > 0:
    if print_labels:
        if line==0:
            print("Printing Column Headers")
        else:
            print("Line " + str(line) + ": writing...")
    getData=str(ser.readline())
    
    data=getData[2:7]
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    file = open(fileName, "a")
    file.write(current_time +" - "+ data + "C"+ '\n') #write data with a newline
    line = line+1

print("Data collection complete!")
file.close()