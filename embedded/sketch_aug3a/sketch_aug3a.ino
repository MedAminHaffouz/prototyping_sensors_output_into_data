#include <DHT.h>

// Pin assignments
const int potPin = A0;
const int buttonPin = 2;
const int dhtPin = 7;
const int dhtType = DHT11;

DHT dht(dhtPin, dhtType);

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT); // Assuming external pull-down resistor
  dht.begin();
}

void loop() {
  // Button is HIGH when pressed
  if (digitalRead(buttonPin) == HIGH) {
    // Read sensor values
    float temp = dht.readTemperature();
    float hum = dht.readHumidity();
    int potValue = analogRead(potPin);

    // Send clean line only if DHT values are valid
    if (!isnan(temp) && !isnan(hum)) {
      Serial.print(temp, 1);        // 1 decimal place
      Serial.print(',');
      Serial.print(hum, 1);
      Serial.print(',');
      Serial.println(potValue);     // Ends with newline
    } else {
      Serial.println("NaN,NaN,NaN"); // Optional: help debug DHT failure
    }

    delay(500); // Basic debounce / avoid spam
  }
}

