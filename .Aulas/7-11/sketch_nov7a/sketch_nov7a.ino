#define BLYNK_TEMPLATE_ID "TMPL2GDECkUcG"
#define BLYNK_TEMPLATE_NAME "IoT Fatec"
#define BLYNK_AUTH_TOKEN "dgd3madcaMqVABaDSFRhxvugJUUx7-Bt"
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp8266.h>
#include <DHT.h>

char ssid[] = "FatecRioClaro";
char pass[] = "FatecRioClaro";
#define DHTPIN 5            // GPIO conectado ao pino de dados do DHT11
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
BlynkTimer timer;
void enviarSensor() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  if (isnan(temperatura) || isnan(umidade)) {
    Serial.println("Falha na leitura do DHT11");
   return;
  }
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
 Serial.print(" °C | Umidade: ");
  Serial.println(umidade);
// Envia para Blynk
  Blynk.virtualWrite(V0, temperatura);
  Blynk.virtualWrite(V1, umidade);
}
void setup() {
  Serial.begin(115200);
  dht.begin();
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
  timer.setInterval(5000L, enviarSensor);  // envia a cada 5 segundos
}
void loop() {
  Blynk.run();
  timer.run();
}
