#define IRpin 2 
#define ledPin 13 

  void setup() { 
    // put your setup code here, to run once: 
  pinMode(IRpin,INPUT); 
  pinMode(ledPin,OUTPUT); 

   Serial.begin(9600);

  } 

  void loop() { 


    int IRread = digitalRead(IRpin);  
    digitalWrite(ledPin,LOW); 
  

  
  if(IRread == 1){ 

    digitalWrite(ledPin,HIGH);
    Serial.print(IRread);

  } 

} 
