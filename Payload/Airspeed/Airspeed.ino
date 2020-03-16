//VERSION 1.0 15 DE MARZO 13:37pm
#include <TinyGPS.h>
#include <Wire.h>
#include <avr/wdt.h>
#include "BlueDot_BME280.h" //esta es la librería utilizada

BlueDot_BME280 bme1;   
BlueDot_BME280 bme2; 
   
//primero se establecen las distintas variables necesarias. Como valor inicial se utiliza 0 pero este irá cambiando
int bme1Detected = 0;     
int bme2Detected = 0;     
int LEDROJO1 = 13;
int LEDAZUL2 = 10; //Ambas LEDS se eliminan para el código final. Se utilizan únicamente para verificar que se toman datos.
int humedad1 = 0;
int humedad2 = 0;
int temperatura1 = 0;
int temperatura2 = 0;
int presion1 = 0;
int presion2 = 0;
int deltapres =0;
int altura1 = 0;
int altura2 = 0;
int presion_vapor = 0;
int presion_aireseco = 0;
int deltaalt = 0; //cambio de las alturas
int long1 = 0; //datos de GPS
int lat1 = 0; // datos de GPS
int long2 = 0; //datos de GPS
int lat2 = 0; // datos de GPS
int radio = 555; //radio de la Tierra para calcular groundspeed
int airspeed = 0;
int groundspeed = 0;
int windspeed = 0;
int density = 0; //densidad del aire

void setup() {
  Serial.begin(9600);
//Todo estos son parámetros que se tienen que declarar para utilizar los sensores BMP280
    bme1.parameter.communication = 0;                    
    bme2.parameter.communication = 0;                   
    bme1.parameter.I2CAddress = 0x77;       
    bme2.parameter.I2CAddress = 0x76;       
    bme1.parameter.sensorMode = 0b11;                    
    bme2.parameter.sensorMode = 0b11;                    
    bme1.parameter.IIRfilter = 0b100;                  
    bme2.parameter.IIRfilter = 0b100;                  
  //Si no se quiere medir humedad  se utiliza factor 0
  //0b000:      factor 0 (Disable humidity measurement)
  //0b101:      factor 16 (default value)
    bme1.parameter.humidOversampling = 0b101;            //Humidity Oversampling for Sensor 1
    bme2.parameter.humidOversampling = 0b101;            //Humidity Oversampling for Sensor 2
 //Si no se quiere medir temperatura se utiliza factor 0
  //0b000:      factor 0 (Disable temperature measurement)
  //0b101:      factor 16 (default value)
    bme1.parameter.tempOversampling = 0b101;              //Temperature Oversampling for Sensor 1
    bme2.parameter.tempOversampling = 0b101;              //Temperature Oversampling for Sensor 2
  //0b000:      factor 0 (Disable pressure measurement)
  //0b101:      factor 16 (default value)  
    bme1.parameter.pressOversampling = 0b101;             //Pressure Oversampling for Sensor 1
    bme2.parameter.pressOversampling = 0b101;             //Pressure Oversampling for Sensor 2 
  //For precise altitude measurements please put in the current pressure corrected for the sea level
    bme1.parameter.pressureSeaLevel = 1013.25;            //default value of 1013.25 hPa (Sensor 1)
    bme2.parameter.pressureSeaLevel = 1013.25;            //default value of 1013.25 hPa (Sensor 2)
  //Also put in the current average temperature outside (yes, really outside!)
  //For slightly less precise altitude measurements, just leave the standard temperature as default (15°C and 59°F);
    bme1.parameter.tempOutsideCelsius = 15;               //default value of 15°C
    bme2.parameter.tempOutsideCelsius = 15;               //default value of 15°C
    bme1.parameter.tempOutsideFahrenheit = 59;            //default value of 59°F
    bme2.parameter.tempOutsideFahrenheit = 59;            //default value of 59°F
  //The Watchdog Timer forces the Arduino to restart whenever the program hangs for longer than 8 seconds.
  //This is useful when the program enters an infinite loop and stops giving any feedback on the serial monitor.
  //However the Watchdog Timer may also be triggered whenever a single program loop takes longer than 8 seconds.
  //Per default the Watchdog Timer is turned off (commented out).
    
  //wdt_enable(WDTO_8S);         
                          
  //Lo que se presenta es para ver si los sensores se detectan y si se puede realizar la medicion. Esto en el código final se puede eliminar
  if (bme1.init() != 0x60)
  {    
    Serial.println(F("Ops! First BME280 Sensor not found!"));
    bme1Detected = 0;
  }
  else
  {
    Serial.println(F("First BME280 Sensor detected!"));
    bme1Detected = 1;
  }
  if (bme2.init() != 0x60)
  {    
    Serial.println(F("Ops! Second BME280 Sensor not found!"));
    bme2Detected = 0;
  }
  else
  {
    Serial.println(F("Second BME280 Sensor detected!"));
    bme2Detected = 1;
  }

  if ((bme1Detected == 0)&(bme2Detected == 0)) //Ninguno de los sensores fue detectado. Muestra posibles errores
  {
    Serial.println();
    Serial.println();
    Serial.println(F("Troubleshooting Guide"));
    Serial.println(F("*************************************************************"));
    Serial.println(F("1. Let's check the basics: Are the VCC and GND pins connected correctly? If the BME280 is getting really hot, then the wires are crossed."));
    Serial.println();
    Serial.println(F("2. Did you connect the SDI pin from your BME280 to the SDA line from the Arduino?"));
    Serial.println();
    Serial.println(F("3. And did you connect the SCK pin from the BME280 to the SCL line from your Arduino?"));
    Serial.println();
    Serial.println(F("4. One of your sensors should be using the alternative I2C Address(0x76). Did you remember to connect the SDO pin to GND?"));
    Serial.println();
    Serial.println(F("5. The other sensor should be using the default I2C Address (0x77. Did you remember to leave the SDO pin unconnected?"));

    Serial.println();
    
    while(1);
  }
    
  Serial.println();
  Serial.println();

}
  //Medición como tal
void loop() {
 
  wdt_reset();//This function resets the counter of the Watchdog Timer. Always use this function if the Watchdog Timer is enabled.
  
  Serial.print(F("Duration in Seconds:  "));
  Serial.println(float(millis())/1000);
  pinMode(LEDROJO1, OUTPUT);
  pinMode(LEDAZUL2, OUTPUT);

  if (bme1Detected) // Para el código final se eliminan los prints y únicamente se cambian los valores de las variables
  {
    digitalWrite(LEDROJO1, HIGH);
    delay(50);
    digitalWrite(LEDROJO1, LOW);
    delay(50);
    Serial.print(F("Temperature Sensor 1 [°C]:\t\t")); 
    temperatura1 = bme1.readTempC();
    Serial.println(temperatura1);
    Serial.print(F("Humidity Sensor 1 [%]:\t\t\t"));
    humedad1 = bme1.readHumidity();
    Serial.println(humedad1);
    Serial.print(F("Pressure Sensor 1 [hPa]:\t\t")); 
    presion1= bme1.readPressure();
    Serial.println(presion1);
    Serial.print(F("Altitude Sensor 1 [m]:\t\t\t")); 
    altura1 = bme1.readAltitudeMeter();
    Serial.println(altura1);
    Serial.println(F("****************************************"));
    digitalWrite(LEDAZUL2, HIGH);
    delay(50);
    digitalWrite(LEDAZUL2, LOW);
    delay(50);    
  }

  else //Esto puede dejarse para comprobar que el sensor se encuentre debidamente conectado
  {
    Serial.print(F("Temperature Sensor 1 [°C]:\t\t")); 
    Serial.println(F("Null"));
    Serial.print(F("Humidity Sensor 1 [%]:\t\t\t")); 
    Serial.println(F("Null"));
    Serial.print(F("Pressure Sensor 1 [hPa]:\t\t")); 
    Serial.println(F("Null"));
    Serial.print(F("Altitude Sensor 1 [m]:\t\t\t")); 
    Serial.println(F("Null"));
    Serial.println(F("****************************************"));   
  }

  if (bme2Detected) // Para el código final se eliminan los prints y únicamente se cambian los valores de las variables
  {
    digitalWrite(LEDROJO1, HIGH);
    delay(50);
    digitalWrite(LEDROJO1, LOW);
    delay(50);
    Serial.print(F("Temperature Sensor 2 [°C]:\t\t"));
    temperatura2 = (float(bme2.readTempC())); 
    Serial.println(temperatura2);
    Serial.print(F("Humidity Sensor 2 [%]:\t\t\t")); 
    humedad2 = (float(bme2.readHumidity()));
    Serial.println(humedad2);
    Serial.print(F("Pressure Sensor 2 [hPa]:\t\t")); 
    presion2 = (float(bme2.readPressure()));
    Serial.println(presion2);
    Serial.print(F("Altitude Sensor 2 [m]:\t\t\t")); 
    altura2 = (float(bme2.readAltitudeMeter()));
    Serial.println(altura2);
    digitalWrite(LEDAZUL2, HIGH);
    delay(50);
    digitalWrite(LEDAZUL2, LOW);
    delay(50);
        
  }

  else //Esto puede dejarse para comprobar que el sensor se encuentre debidamente conectado
  {
    Serial.print(F("Temperature Sensor 2 [°C]:\t\t")); 
    Serial.println(F("Null"));
    Serial.print(F("Humidity Sensor 2 [%]:\t\t\t")); 
    Serial.println(F("Null"));
    Serial.print(F("Pressure Sensor 2 [hPa]:\t\t")); 
    Serial.println(F("Null"));
    Serial.print(F("Altitude Sensor 2 [m]:\t\t\t")); 
    Serial.println(F("Null"));
  }
   presion_vapor = ((6.1078*pow(10,((7.5*temperatura2)/(temperatura2+237.32))))*(humedad2/100));
   presion_aireseco= (presion2-presion_vapor);
   density = ((presion_aireseco/287.058*(temperatura2+273.15))+(presion_vapor/461.495*(temperatura2+273.15))); //calculo de la densidad del aire
   deltapres = abs(presion1-presion2);
   airspeed=(sqrt((deltapres)/density)); //Ecuacion de Bernoulli
   Serial.print(F("Airspeed (m/s)=")); //Print no necesario para el código final
   Serial.println(airspeed); //Print no necesario para el código final
   //Recolectar datos de longitud y latitud con GPS
   long1 = 0; 
   lat1 = 0; 
   long2 = 0; 
   lat2 = 0; 
   groundspeed = TinyGPS::distance_between(lat1,long1,lat2,long2); //formula de groundspeed. Se utiliza la fórmula del semiverseno
   //Este groundspeed no considera el cambio de altura, por lo que se debe de hacer aparte
   deltaalt =abs(altura1-altura2);
   groundspeed = sqrt(pow(groundspeed,2)+pow(deltaalt,2)); //esto es lo equivalente a calcular la magnitud del vector velocidad
   Serial.print(F("Groundspeed (m/s)="));//Print no necesario para el código final
   Serial.println(groundspeed);//Print no necesario para el código final
   windspeed = (groundspeed - airspeed);
   Serial.print(F("Wind speed (m/s)="));
   Serial.println(windspeed); //esto es lo único que se ocupa retornar de todo el programa
   
   Serial.println();
   Serial.println();

   delay(1000);
   
 
}
