/* Alvaro Bermudez
 * Projecto Cansat 2020 - 
 * Sistema de release utilizando el altimetro del sensor bmp280
 * 
 * Resumen del codigo
 * El codigo lee altura cada segundo y determina si esta en un rango de altura y si esta bajando 
 * Cuando las 3 condiciones se cumplen da una señal HIGH a un pin que esta conectado al cable de nicromio durante 5 segundos
 * 
 * Se necesita añadir el codigo para que se active el audiobeacon/buzzer
 * Para hacer las pruebas modificar los rangos de altura para determinar si el codigo funciona como se desea
 * 
 * 
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

void loop() {
    Serial.print(bmp.readTemperature());                          /*no necesita leer temperatura y presion pero por si acaso*/
    Serial.print(bmp.readPressure());

    H_actual = bmp.readAltitude(1013.25);

    if (H_actual>100 && H_actual>H_anterior && H_actual<450);     /*necesita 3 condiciones para dar la señal HIGH*/
    {                                                             /*que este entre el rango de 100 a 450 metros y bajando*/
      digitalWrite(2,HIGH);
      delay(5000);
    }
    H_anterior = H_actual;                                        /*despues de que compara alturas reescribe la altura actual como la anterior para el siguiente ciclo*/
    Serial.println();
    delay(1000);                                                  /*delay 1 Hz*/
}
