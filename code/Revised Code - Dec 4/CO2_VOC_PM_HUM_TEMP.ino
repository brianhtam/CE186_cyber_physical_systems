
//Temperature & Humidity
#include <Wire.h>
#include "cactus_io_HIH6130.h"
//define the address used by the HIH6130 sensor (default is 0x27)
byte address = 0x27;
//Set up an instance of the sensor
HIH6130 hih6130(address);

//CO2 & VOC
#include "SparkFunCCS811.h"
#define CCS811_ADDR 0x5B //Default I2C Address#include "SparkFunCCS811.h"
CCS811 mySensor(CCS811_ADDR);

///////////
int measurePin = 0; 
int ledPower = 2; 

int samplingTime = 280; 
int deltaTime = 40; 
int sleepTime = 9680;

float voMeasured = 0; 
float calcVoltage = 0; 
float dustDensity = 0; 

////////////

void setup(){
  Serial.begin(9600);

////////////
  pinMode(ledPower, OUTPUT); 
///////////

  //CO2 & VOC
  //It is recommended to check return status on .begin(), but it is not
  //required.
  CCS811Core::status returnCode = mySensor.begin();
  if (returnCode != CCS811Core::SENSOR_SUCCESS)
  {
    Serial.println(".begin() returned with an error.");
    while (1); //Hang if there was a problem.
  }
}
  
void loop(){

//////////////
digitalWrite(ledPower,LOW); 
delayMicroseconds(samplingTime); 

voMeasured = analogRead(measurePin);

delayMicroseconds(deltaTime); 
digitalWrite(ledPower,HIGH); 
delayMicroseconds(sleepTime); 

calcVoltage = voMeasured * (5.0 / 1024.0); 

dustDensity = 0.17 * calcVoltage; 

//////////////


//Check to see if data is ready with .dataAvailable()
  if (mySensor.dataAvailable())
  {
    //If so, have the sensor read and calculate the results.
    //Get them later
    mySensor.readAlgorithmResults();
    //Returns calculated CO2 reading
    Serial.print(mySensor.getCO2());
    Serial.print(",");
    Serial.print(mySensor.getTVOC());
    Serial.print(",");
  }

    Serial.print(dustDensity); 
    Serial.print(",");


// Read the data -> stored to public variables
hih6130.readSensor();
  
// Access the variables and print to serial monitor
Serial.print(hih6130.humidity); 
Serial.print(",");
Serial.print(hih6130.temperature_C); 
Serial.println();


  delay(2000);
}
