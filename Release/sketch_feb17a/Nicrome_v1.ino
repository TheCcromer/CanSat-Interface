/*Alvaro Bermudez
 * Projecto Cansat 2020 - Tucan 2 - Grupo Ingenieria Aeroespacial - Universidad de Costa Rica
 * Configuracion para el cable de nicromio:
 * 
 * Resumen del codigo y notas de hardware
 * El codigo es basicamente un blink para hacer pruebas, solo necesita una salida HIGH para controlar el releay de 5v
 * El nicromio a 5v y 3cm de largo corta el nilon de 3 a 4 segundos, esto puede variar por cuestiones de temperatura ambiente y presion atmosferica local
 * La coneccion del hardware del nicromio es de
 *  Salida arduino > transistor > relay > bateria/5V del arduino (3V es muy poco) > nicromio
 * Si se utilizan 9V es mas rapido pero consume mucha corriente por lo que puede generar un corto, para evitar eso se puede añadir una resistencia para bajar la corriente
 * Con una resistencia de aproximadamente 0.1 ohms y 5V de tension utiliza 50 amperios de corriente aproximadamente, es mucha corriente por lo que hay que tener cuidado
 * Entre mas corto el cable de nicromio es mejor, mas rapido de calentar y mas seguro
 * 
 */



const int LEDPin= 13;

void setup() {
  Serial.begin(9600);                     
  pinMode(LEDPin, OUTPUT);
  
}
void loop() {                             
               
  digitalWrite(LEDPin, HIGH);            
  delay(4000);               
  digitalWrite(LEDPin, LOW);
  delay(10000);             
}
