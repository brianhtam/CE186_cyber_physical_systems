/*
  HIH6130.h - Library for reading relative humidity and temperature data 
  This file was derived from the by David H Hagan library
  
  Use as you like. MIT license.
*/

#ifndef HIH6130_h
#define HIH6130_h

#include <Arduino.h>

class HIH6130 {

private:
    uint8_t _address;
    uint8_t _humidity_lo, _humidity_hi;
    uint8_t _temp_lo, _temp_hi;
    uint8_t _status;
    
public:
    HIH6130(uint8_t address);
    void begin();
    void readSensor();
    float computeHeatIndex_C(void);
    float computeHeatIndex_F(void);

    float humidity;
    float temperature_C;
    float temperature_F;
    
};

#endif