# Import requests (used to access API).
import requests

# Import serial (used to communicate with arduino over USB).
import serial

# Desired tickers are included in this array.
tickers = ["ETH", "BTC", "ADA"]

# Get number of tickers.
numTickers = len(tickers)

# Setup serial port and name it "arduino", using 115200 baud.
# The serial port may need to be changed to suit your system (here it is 'COM7')
arduino = serial.Serial('COM7', 115200, timeout = 0.5)

# Function to request data for a ticker from an api and then send it over the serial port
def sendData(tickerNum):

    # Get a request for the ticker from the Api.
    apiRequest = requests.get("https://api.binance.us/api/v3/ticker/24hr?symbol=" + tickers[tickerNum] + "USD").json()
    
    # Indicator variable describing whether the price change is positive or negative.
    # 1 denotes positive, 0 denotes negative.
    priceChangePositive = float(apiRequest["priceChangePercent"]) > 0

    # Denotes the symbol being displayed.
    symbol = tickers[tickerNum][0:3]

    # Creating the percent price change (adding a "+" if positive, and a "%" regardless of sign).
    if (priceChangePositive):
        priceChangePercent = "+" + str(round(float(apiRequest["priceChangePercent"]), 2)) + "%"
    else:
        priceChangePercent = str(round(float(apiRequest["priceChangePercent"]), 2)) + "%"

    # Denotes the last price of the symbol.
    lastPrice = str(round(float(apiRequest["lastPrice"]), 3))

    # Initializes a variable that will contain the necessary number of spaces
    # needed to achieve the proper spacing on the LCD.
    necessarySpaces = ""

    # Fills necessarySpaces with the proper number of spaces needed for line 1 on the LCD.
    for i in range(16 - len(symbol) - len(priceChangePercent)):
        necessarySpaces = necessarySpaces + " "

    # Constructs the 1st line to be displayed on the LCD: 
    firstLine = symbol + necessarySpaces + priceChangePercent

    # Resets necessarySpaces to an empty string
    necessarySpaces = ""

    # Fills necessarySpaces with the proper number of spaces needed for line 2 on the LCD.
    for i in range(16 - len("Price:" + '$' + lastPrice)):
        necessarySpaces = necessarySpaces + " "

    # Constructs the 2nd line to be displayed on the LCD: 
    secondLine = "Price:" + necessarySpaces + "$" + lastPrice

    # Combines firstLine and secondLine into a comma-separated string
    # This will be sent to the arduino and then interpreted.
    dataToSend = firstLine + ',' + secondLine + ','

    # Send string to arduino via serial port
    arduino.write(str.encode(dataToSend))

# Track the index value of the next ticker to be sent.  
nextTicker = 0

# This is the main loop that will check for data requests from the Arduino.
while (1):

    # If the arduino sends a signal to the computer through the serial port,
    # check that it is requesting data.
    if (arduino.in_waiting > 0):

        # If the arduino is requesting data, get the data from the api and then send it.
        if (int.from_bytes(arduino.read(), "big")):
            sendData(nextTicker)

            # If the last ticker in tickers array has been sent, set nextTicker = 0.
            # Else increase nextTicker's value by 1 so that the next ticker is
            # sent next time sendData is called.
            if (nextTicker == numTickers - 1):
                nextTicker = 0
            else: 
                nextTicker += 1