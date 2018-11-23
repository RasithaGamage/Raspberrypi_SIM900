#!/usr/bin/env python
import serial
import time
import sys
import subprocess
import os
import signal

phoneNum = sys.argv[1];
message = sys.argv[2];


ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=None
)

ser.write(('ATD'+phoneNum+';'+'\r\n').encode())
time.sleep(5)

flag = 0;
result = "";

while(1):
        result = ser.readline()
        if result.strip()=='OK':
            if flag <= 1:
                
                sudoP = 'raspberry'
                command = 'gtts-cli "%s" -o /home/pi/Desktop/ims_temp.mp3'%message
                os.system('echo %s|sudo -S %s' % (sudoP,command))
                
                time.sleep(10)
                
                os.system('echo %s|sudo -S %s' % (sudoPassword,'mpg321 -o alsa --loop 2 /home/pi/Desktop/ims_temp.mp3'))
                os.system('echo %s|sudo -S %s' % (sudoPassword,'rm /home/pi/Desktop/ims_temp.mp3'))
 

                ser.write(('ATH\r\n').encode())
                while(1):
                    result = ser.readline()
                    if result.strip()=='OK':
                        print("CALL ENDED")
                        break
                    
                    if result.strip()=='BUSY':
                        print(result)
                        break
                    
                    if result.strip()=='NO ANSWER':
                        print(result)
                        break
                    
                    if result.strip()=='NO CARRIER':
                        print(result)
                        break
                break
            
            flag=flag+1;
     
#OK #BUSY #NO ANSWER #NO CARRIER     
ser.flush()
ser.close()
