/*
  AnalogReadSerial

 Modified by: Matthew (pan) Choi

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  int milivolt = sensorValue*(5000/1024);
  int T = (milivolt - 500)/10;
  int F = T*(9/5) + 32;
  int R = random(0,15);//Random number generation
  int RR = random(0,13);
  int RRR = random(0,10); 
  int RRRR = random(0,15);
  // print out the value you read:
  Serial.print(T);
  Serial.print(",");
  Serial.print(T+R);
  Serial.print(",");
  Serial.print(T+RR);
  Serial.print(",");
  Serial.print(T+RRR);
  Serial.print(",");
  Serial.print(T+RRRR);
  Serial.println();
  delay(1000);        // delay in between reads for stability
}
