/*
  HIH6130.cpp - This library was derived from the Library Created by David H Hagan, November 22, 2014.
  
  Use as you like. MIT license.
*/

#include <Arduino.h>
#include "cactus_io_HIH6130.h"
#include <Wire.h>

HIH6130::HIH6130(uint8_t address)
{
	_address = address;
	_humidity_lo = 0;
	_humidity_hi = 0;
	_temp_hi = 0;
	_temp_lo = 0;
	_status = 0;
}

void HIH6130::begin(){
	
	// setup the HIH6130 sensor
	Wire.begin();
}

void HIH6130::readSensor(){
	// reads data from the sensor and stores them in temporary variables that
	// are then accessed via public variables
	Wire.beginTransmission(_address);
	Wire.endTransmission();

	Wire.requestFrom( (int) _address, (int) 4);
	while (Wire.available() == 0);

	_humidity_hi = Wire.read();
	_humidity_lo = Wire.read();
	_temp_hi = Wire.read();
	_temp_lo = Wire.read();

	Wire.endTransmission();

	// Get the status (first two bits of _humidity_hi_)
	_status = (_humidity_hi >> 6);

	// Calculate Relative Humidity
	humidity = (float)(((unsigned int) (_humidity_hi & 0x3f) << 8) | _humidity_lo) * 100 / (pow(2,14) - 1);

	// Calculate Temperature
	temperature_C = (float) (((unsigned int) (_temp_hi << 6) + (_temp_lo >> 2)) / (pow(2, 14) - 1) * 165 - 40);
    
    // Calculate Temperate in Fahrenheit. Using the formula F = C * 1.8 + 32
    temperature_F = temperature_C * 1.8 + 32;
}

float HIH6130::computeHeatIndex_C(void) {
    // Wikipedia: http://en.wikipedia.org/wiki/Heat_index
    return -8.784695 +
    1.61139411 * temperature_C +
    2.33854900 * humidity +
    -0.14611605 * temperature_C*humidity +
    -0.01230809 * pow(temperature_C, 2) +
    -0.01642482 * pow(humidity, 2) +
    0.00221173 * pow(temperature_C, 2) * humidity +
    0.00072546 * temperature_C * pow(humidity, 2) +
    -0.00000358 * pow(temperature_C, 2) * pow(humidity, 2);
}

float HIH6130::computeHeatIndex_F(void) {
    // Adapted from equation at: https://github.com/adafruit/DHT-sensor-library/issues/9 and
    // Wikipedia: http://en.wikipedia.org/wiki/Heat_index
    return -42.379 +
    2.04901523 * temperature_F +
    10.14333127 * humidity +
    -0.22475541 * temperature_F*humidity +
    -0.00683783 * pow(temperature_F, 2) +
    -0.05481717 * pow(humidity, 2) +
    0.00122874 * pow(temperature_F, 2) * humidity +
    0.00085282 * temperature_F*pow(humidity, 2) +
    -0.00000199 * pow(temperature_F, 2) * pow(humidity, 2);
}
