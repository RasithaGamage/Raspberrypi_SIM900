#!/usr/bin/env python
import serial
import time
import sys
import subprocess
import os
import signal
from pathlib import Path



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
                            
sudoP = 'raspberry'
command = 'gtts-cli "%s" -o /home/pi/Desktop/ims_temp.mp3'%message
os.system('echo %s|sudo -S %s' % (sudoP,command))
                            
ser.write(('ATD'+phoneNum+';'+'\r\n').encode())
time.sleep(5)

result = ""

dialing = 'false'
answered = 'false'
cut = 'false'

automaticCut ='false'

carrierResponse = 'null'

while(1):
        result = ser.readline()
        if result.strip()=='OK':
                while(1):
                    result = ser.readline()
                    checkVar1 = result.split(' ', 1 )
                    
                    if checkVar1[0]=='+CLCC:':
                        checkVar2 = result.split(',', 3 )
                        
                        if checkVar2[2]=='3': #call dialing
                            dialing = 'true'
                            
                        if checkVar2[2]=='0': #call answered
                            answered = 'true'

                        if checkVar2[2]=='6': #call cut
                            cut='true'
                            
                        if answered=='true' :
                            file_path = Path("/home/pi/Desktop/ims_temp.mp3")
                            if file_path.is_file():
                                p = subprocess.Popen(["mpg321","-o","alsa","--loop","2","/home/pi/Desktop/ims_temp.mp3"],stdout=subprocess.PIPE, stdin = subprocess.PIPE, stderr=subprocess.STDOUT)
                                p.wait()
                                os.system('echo %s|sudo -S %s' % (sudoP,'rm /home/pi/Desktop/ims_temp.mp3'))
                            
                            ser.write(('ATH\r\n').encode())
                            
                            
                            while(1):
                                 result = ser.readline()
                                 
                                 if result.strip()=='ATH':
                                     automaticCut = 'true'
                                     carrierResponse='CALL FINISHED'
                                     
                                 checkVar3 = result.split(' ', 1 )
                                 if checkVar3[0]=='+CLCC:':
                                     checkVar4 = result.split(',', 3 )
                                     if checkVar4[2]=='6':
                                         cut='true'
                                         break
                            
                        
                        if cut=='true':
                            break   
                            
                if automaticCut == 'false':            
                    while(1):
                        
                        if carrierResponse=='CALL FINISHED':
                            break
                                     
                        result = ser.readline()
                        
                        if result.strip()=='BUSY':
                            carrierResponse='BUSY'
                            break
                        
                        if result.strip()=='NO ANSWER':
                            carrierResponse='NO ANSWER'
                            break
                        
                        if result.strip()=='NO CARRIER':
                            carrierResponse='NO CARRIER'
                            break

                        if result.strip()=='ERROR':
                            carrierResponse='ERROR'
                            break
                    
                    
        if (dialing=='true'):
            print("ANS:"+answered+" "+carrierResponse)
            break;

        
#OK #BUSY #NO ANSWER #NO CARRIER     
ser.flush()
ser.close()
