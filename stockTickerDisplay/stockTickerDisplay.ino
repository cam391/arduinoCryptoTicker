// Include the lcd library:
#include <LiquidCrystal.h>

// Create an LCD object. Parameters: (RS, E, D4, D5, D6, D7):
LiquidCrystal lcd = LiquidCrystal(2, 3, 4, 5, 6, 7);

// Desired display time (in seconds)
displayTime = 12

// String array of data to be displated on the lcd.
String displayData[2];

void setup() {
  // Specify the LCD's number of columns and rows.
  lcd.begin(16, 2);

  // Set up serial w/ computer.
  Serial.begin(115200);

}

void loop() {

  // If the computer has sent something over the serial port.
  if (Serial.available() > 0) {

    // Wait half the desired display time
    delay(displayTime*500);

    // Read data from serial port into displayData array.
    for (int i = 0; i < 2; i++) {
      displayData[i] = Serial.readStringUntil(',');
    }

    // Clear display.
    lcd.clear();

    // Set cursor to first line.
    lcd.setCursor(0, 0);

    // Print ticker and percent change.
    lcd.print(displayData[0]);

    // Set cursor to second line.
    lcd.setCursor(0, 1);

    // Print last price.
    lcd.print(displayData[1]);

  }

  // Send a 1 to computer (requests next ticker).
  Serial.write(1);

    // Wait half the desired display time
  delay(displayTime*500);
}
