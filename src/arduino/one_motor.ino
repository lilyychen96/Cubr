// defines pins numbers
const int stepPin = 3; 
const int dirPin = 4; 
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
}

void F1turn() {
  digitalWrite(dirPin,HIGH);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(500); 
  }
}

void F2turn() {
  digitalWrite(dirPin,LOW);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(500); 
  }
}

void F3turn() {
  digitalWrite(dirPin,HIGH);
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(500); 
  }
}

void loop() {
 
  F1turn();
  delay(1000); // One second delay
  F3turn();
  delay(1000);
}
