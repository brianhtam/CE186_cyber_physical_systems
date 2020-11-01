#include <Wire.h>
#include "cactus_io_HIH6130.h"
 
//define the address used by the HIH6130 sensor (default is 0x27)
byte address = 0x27;
 
//Set up an instance of the sensor
HIH6130 hih6130(address);

void setup(){
Serial.begin(9600);
Serial.println("Honeywell HIH6130 Humidity - Temperature Sensor");
Serial.println("RH\tTemp (C)\tTemp (F)\tHeat Index (C)\tHeat Index (F)");
}
  
void loop(){
// Read the data -> stored to public variables
hih6130.readSensor();
  
// Access the variables and print to serial monitor
Serial.print(hih6130.humidity); 
Serial.print("\t");
Serial.print(hih6130.temperature_C); 
Serial.print("\t\t");
Serial.print(hih6130.temperature_F);
Serial.print("\t\t");
Serial.print(hih6130.computeHeatIndex_C());
Serial.print("\t\t");
Serial.print(hih6130.computeHeatIndex_F());
Serial.println(); 
// 3 second delay
delay(3000);
}
