#include <Wire.h>
#include "DFRobot_SHT20.h"
int value = 0;

DFRobot_SHT20    sht20;

void setup()
{
    Serial.begin(9600);
    sht20.initSHT20();                                  // Init SHT20 Sensor
}

void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     
     if (value == '1')
        {
          float temp = sht20.readTemperature();               // Read Temperature
          Serial.print(temp);
          Serial.println();
        }
     
     else if (value == '2')
        {
         float humd = sht20.readHumidity();                  // Read Humidity
         Serial.print(humd);
         Serial.println(); 
         }
     
   
   }
