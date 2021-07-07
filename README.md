# arduinoCryptoTicker

<H2>Introduction</h2>

<p>
A simple cryptocurrency ticker using an arduino uno and a 16x2 LCD display.
  
The project works through using a computer to access price and price change data through <a href="https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md">Binance's API</a>, and then sending the data over a USB serial port to the arduino upon request. The arduino then parses the data sent from the computer, and displays it on a 16x2 LCD.
</p>

<h2>Hardware</h2>

<p>
 The hardware used is as follows:
  
  - 1 Arduino Uno
  - 1 USB-A to USB-B Cable
  - 1 Breadboard
  - 13 Male to Male Jumpers
  - 1 10k Potentiometer
  - 1 Laptop/Desktop with internet capability and a USB-A port
  - 1 LCD 1602 Module with Pin Header
  
<h2>Hardware Setup</h2>
  
<p> 
The appropriate setup for the arduino and LCD can be found in this tutorial: https://www.makerguides.com/character-lcd-arduino-tutorial/.
  
Finally, just plug the USB-A to USB-B cable into your arduino and computer respectively.
</p>

<h2>Software Overview</h2>

<p> 
There are two files necessary to make this project work:
  
The first - "stockDataRequest.py" - runs on the computer and performs the task of requesting data from Binance's API and sending it to the arduino over the serial port when requested.
  
The second - "stockTickerDisplay.ino" runs on the arduino and sends requests to the computer and then recieves and displayes the data on the LCD.
</p>

<h2>Software Setup</h2>

<p>
With the arduino connected to the computer via the USB cable, open "stockTickerDisplay.ino" in the <a href="https://www.arduino.cc/en/software">arduino IDE</a>. Upload the file to the arduino using the upload button.

Now, run "stockDataRequest.py" and watch as the LCD begins to display the desired crypto data.
</p>

<h2>Troubleshooting and Customization</h2>

<p>
- Note that the serial port must be correct for the project to work, and must be the same in both the .ino and .py files. If the incorrect port is being used, go to the arduino ide and click "Tools". Then click "Port" and select the port that has "(arduino uno)" bedside it. Then edit the files with the name of the port (i.e. from "COM7" to "COM2").

- Note that the baud rates may be changed, but they must be the same in each file. The original baud rate of 115200 should work in most cases.
  
- To change the crypto symbols being used, edit the tickers array in "stockDataRequest.py" on line 8. Just be sure that the symbol used is the same as the symbol used by binance. Also note that all currencies are displayed in USD ($). This can be changed by editing the API request URL in "stockDataRequest.py" on line 21, as well as changing the dollar-sign to the desired notation on line 58.
  
- The display time of each currency can be changed by editing line 8 in "stockTickerDisplay.ino"
</p>
 
