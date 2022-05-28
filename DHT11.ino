#include "DHT.h"
#define DHTPIN 2 

DHT dht(DHTPIN, DHT11);

void setup(){
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  dht.begin(); 
}

void loop(){ 
    delay(2000);
    float t = dht.readTemperature();
    float d = dht.readHumidity();
    if (isnan(t)){
      Serial.println("Ошибка темометр сдох :(");
      return;
      }
    Serial.print(t);
    Serial.print(d);
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    delay(500); 
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
} 
