// defines pins numbers
const byte numChars = 200;
char receivedChars[numChars];

boolean newData = false;

const int turnSpeed = 1000;
const int turnDelay = 1500;
const int stepPinF = 8; 
const int dirPinF = 9; 
const int stepPinR= 6; 
const int dirPinR = 7; 
const int stepPinL= 12; 
const int dirPinL = 13; 
const int stepPinB= 4; 
const int dirPinB = 5;
const int stepPinU= 2; 
const int dirPinU = 3;
const int stepPinD= 10; 
const int dirPinD = 11;   


void setup() {
  Serial.begin(9600);
  Serial.println("<Arduino is ready>");
//   Sets the two pins as Outputs
  pinMode(stepPinF,OUTPUT); 
  pinMode(dirPinF,OUTPUT);
  pinMode(stepPinR,OUTPUT); 
  pinMode(dirPinR,OUTPUT);
  pinMode(stepPinL,OUTPUT); 
  pinMode(dirPinL,OUTPUT);
  pinMode(stepPinB,OUTPUT); 
  pinMode(dirPinB,OUTPUT);
  pinMode(stepPinU,OUTPUT); 
  pinMode(dirPinU,OUTPUT);
  pinMode(stepPinD,OUTPUT); 
  pinMode(dirPinD,OUTPUT);
}

void F1turn() {
  digitalWrite(dirPinF,HIGH);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinF,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinF,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void F2turn() {
  digitalWrite(dirPinF,LOW);
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPinF,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinF,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void F3turn() {
  digitalWrite(dirPinF,LOW);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinF,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinF,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void R1turn() {
  digitalWrite(dirPinR,HIGH);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinR,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinR,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void R2turn() {
  digitalWrite(dirPinR,LOW);
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPinR,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinR,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void R3turn() {
  digitalWrite(dirPinR,LOW);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinR,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinR,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void L1turn() {
  digitalWrite(dirPinL,HIGH);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinL,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinL,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void L2turn() {
  digitalWrite(dirPinL,LOW);
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPinL,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinL,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void L3turn() {
  digitalWrite(dirPinL,LOW);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinL,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinL,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void B1turn() {
  digitalWrite(dirPinB,HIGH);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinB,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinB,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void B2turn() {
  digitalWrite(dirPinB,LOW);
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPinB,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinB,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void B3turn() {
  digitalWrite(dirPinB,LOW);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinB,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinB,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void U1turn() {
  digitalWrite(dirPinU,HIGH);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinU,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinU,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void U2turn() {
  digitalWrite(dirPinU,LOW);
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPinU,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinU,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void U3turn() {
  digitalWrite(dirPinU,LOW);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinU,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinU,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void D1turn() {
  digitalWrite(dirPinD,HIGH);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinD,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinD,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void D2turn() {
  digitalWrite(dirPinD,LOW);
  for(int x = 0; x < 100; x++) {
    digitalWrite(stepPinD,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinD,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void D3turn() {
  digitalWrite(dirPinD,LOW);
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinD,HIGH); 
    delayMicroseconds(turnSpeed); 
    digitalWrite(stepPinD,LOW); 
    delayMicroseconds(turnSpeed); 
  }
}

void loop() {
    recvWithStartEndMarkers();
    showNewData();
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                if (receivedChars[ndx] == 'Q') {
                    F1turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'W') {
                    F2turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'E') {
                    F3turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'R') {
                    R1turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'T') {
                    R2turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'Y') {
                    R3turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'U') {
                    B1turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'I') {
                    B2turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'O') {
                    B3turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'P') {
                    L1turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'A') {
                    L2turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'S') {
                    L3turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'D') {
                    U1turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'F') {
                    U2turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'G') {
                    U3turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'H') {
                    D1turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'J') {
                    D2turn();
                    delay(turnDelay);              
                }
                else if (receivedChars[ndx] == 'K') {
                    D3turn();
                    delay(turnDelay);              
                }
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
        Serial.print("This just in ... ");
        Serial.println(receivedChars);
        newData = false;
    }
}
