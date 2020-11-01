/*
  AnalogReadSerial

Modified by: Matthew Choi

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

const int buttonPin = 2; 
const int ledPin = 9; 

int buttonState = 0; 

void setup(){
  pinMode(ledPin, OUTPUT); 
  pinMode(buttonPin, INPUT); 
  Serial.begin(9600);
}

//

void loop(){
    int tempValue = analogRead(A2);
    int milivolt = tempValue*(5000/1024); 
    int T = (milivolt - 500)/10; 
    int lightValue = analogRead(A0); 
    int brightness = map(lightValue, 0,1023,0,255); 
    Serial.print(lightValue);
    Serial.print(","); 
    Serial.println(T);

    if (Serial.available()>0){
      int incomingByte=Serial.parseInt(); 
      analogWrite(ledPin,incomingByte);
    }
   // else {
  //   analogWrite(ledPin,0);
  //  }
    delay(1000);
}



