/* Alvaro Bermudez
 * Projecto Cansat 2020 - 
 * Sistema de fases utilizando el altimetro del sensor bmp280
 * 
 * Resumen del codigos
 * El codigo se divide en 3 fases: despegue y descenso, toma de datos y aterrizaje
 
 * Cuando el codigo inicia esta en fase 0, despegue y descenso
 * El codigo lee altura cada segundo y determina si esta en un rango de altura y si esta bajando 
 * Cuando las 3 condiciones significa que el payload se ha liberado y cambia de fase
 * 
 
 * La fase 1 es toma de datos en la que usa los sensores, envia los datos a la GCS y guarda datos en la eemprom
 * Cuando el minuto de vuelo pase cambiad de fase y deja de usar los sensores
 
 * La ultima fase de aterrizaje nada mas mide la altura y cuando sea menonr a 10m activa el audio beacon
 
 * Se necesita añadir el codigo para que se active el audiobeacon/buzzer
 * Para hacer las pruebas modificar los rangos de altura para determinar si el codigo funciona como se desea
 
 */
/*Librerias y setups necesarios*/

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>

#define BMP_SCK  (13)
#define BMP_MISO (12)
#define BMP_MOSI (11)
#define BMP_CS   (10)

Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);

void setup() {
  pinMode(2,OUTPUT);
  Serial.begin(9600);
  Serial.println(F("BMP280 test"));

  if (!bmp.begin()) {
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring!"));
    while (1);
  }

  /* Default settings from datasheet. */
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */
}

float H_anterior = 0;
float H_actual = 0;

int fase = 0;

void loop() {
  /* fase despegue y descenso*/
  if (fase == 0);
  {
    Serial.print(bmp.readTemperature());                          /*no necesita leer temperatura y presion pero por si acaso*/
    Serial.print(bmp.readPressure());
    H_actual = bmp.readAltitude(1013.25);
    if (H_actual>100 && H_actual>H_anterior && H_actual<450);     /*necesita 3 condiciones para dar la señal HIGH*/
    {                                                             /*que este entre el rango de 100 a 450 metros y bajando*/
      fase = fase + 1                                             /*cambio de fase*/
    }
    H_anterior = H_actual;                                        /*despues de que compara alturas reescribe la altura actual como la anterior para el siguiente ciclo*/
    Serial.println();
    delay(1000);                                                  /*delay 1 Hz*/
  }
  /*fase de toma de datos. Aca se puede añadir los sensores, el envio de datos al XBEE y almacenamiento en eeprom
  */
  if (fase == 1);  
  {
      
  }
  /*fase de toma de aterrizaje, añadir solamente la activacion del audiobeacon*/
  if (fase == 2);
  {
   H_actual = bmp.readAltitude(1013.25);
   if (H_actual<10);{
   
   }
  }
}
