const int LEDPin= 13;

void setup() {
  Serial.begin(9600);                     
  pinMode(LEDPin, OUTPUT);
  
}
void loop() {                             
               
  digitalWrite(LEDPin, HIGH);            
  delay(10000);               
  digitalWrite(LEDPin, LOW);
  delay(2000);             
}
