#define IRpin1 11 
#define IRpin2 10
#define ledPin 13

int personCount = 0;
int waitTime = 500;

  void setup() { 
    // put your setup code here, to run once: 
  pinMode(IRpin1,INPUT); 
  pinMode(IRpin2,INPUT); 

  pinMode(ledPin,OUTPUT); 

   Serial.begin(9600);
  } 

  void loop() { 

      int IRread1 = digitalRead(IRpin1);  // First Sensor 
      int IRread2 = digitalRead(IRpin2);

      if(IRread1 == 0) {

        if(personCount > 0) {

          while(true) {

          IRread2 = digitalRead(IRpin2);  // Second Sensor

          if(IRread2 == 0) {
            Serial.println("Rausgehen");
            personCount--;
            /*
            Serial.print("Person Count: ");
            Serial.println(personCount);
            */
            break;
          }

        }
        IRread1 = 1;
        IRread2 = 1;
        delay(waitTime);

        }
        
      }

      IRread1 = digitalRead(IRpin1);  // First Sensor 
      IRread2 = digitalRead(IRpin2);  // Second Sensor

      if(IRread2 == 0) {

        while(true) {
          
          IRread1 = digitalRead(IRpin1);  // First Sensor 

          if(IRread1 == 0) {
            Serial.println("Reingehen");
            personCount++;
            /*
            Serial.print("Person Count: ");
            Serial.println(personCount);
            */
            break;
          }

        }

        delay(waitTime);
        IRread1 = 1;
        IRread2 = 1;

      }
      
  }