# Raspberrypi_SIM900
Generate automatic voice calls with Raspberry pi and SIM900 GSM module

<h3>USED COMPONENTS</h3>

</ul>
  <li>Raspberry Pi 3 </li>
  <li>SIM900 Arduino GSM shield</li>
  <li>USB TTL converter (CH340G)</li>
  <li>AUX cable</li>
</ul>
<h5>Setting up hardwares</h5>
</ul>
  <li>USB TTL converter is used to transmit data between RPI3 and SIM900</li>
  <li>Audio OUT of the RPI3 is connected to Audio IN of SIM900</li>
  <li>Install minicom and check the GSM module with some ATcommands to ensure the right connection</li>
   <ol>
     <li>sudo apt-get install minicom  
           <ul>
             <li>check: https://www.tldp.org/HOWTO/Remote-Serial-Console-HOWTO/modem-minicom.html</li>
          </ul>
     <li>Enable CLCC </li>
           <ul>
             <li>AT+CLCC=1</li>
           </ul>  
     <li>making a call</li>
         <ul>
           <li>AT</li>
           <li>ATD +9471XXXXXXX;</li>
         </ul>
   </ol>   
</ul>

<h5>Configuring RPI3</h5>
</ul>
  <li>sudo apt-get install mpg321</li>
  <li>sudo pip install pathlib</li>
  <li>sudo pip install gTTS</li>
  <li>sudo apt-get install alsa-utils</li>
  <li>sudo apt-get install alsa-oss</li>
</ul>
<h5>How to run python program</h5>
</ul>
  <li>Change directory to the location where python script exists</li>
  <li>Run:   sudo python call.py +9471XXXXXXX "your message"</li>
</ul>


<p>Note: Voice was too noisy at first, as the solution, GSM module powered using an external power supply. Then ground pin of GSM module is connected to RPI ground and eventually annoying noise got removed.</p>
