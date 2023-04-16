#include <Servo.h>
// Left Servo
Servo myservo2;
Servo myservo3;
// Right Servo
Servo myservo4;
Servo myservo5;
int pos = 0;    // variable to store the servo position
int sos = 0; 
int jos = 0;
int tos = 0;
void setup() {
Serial.begin(9600);
//Left Side
myservo2.attach(3);  // attaches the servo on pin 9 to the servo object
myservo3.attach(5);
//Right Side  
myservo4.attach(9);  // attaches the servo on pin 9 to the servo object
myservo5.attach(11);

myservo5.write(90);
myservo4.write(90);
myservo3.write(170);
myservo2.write(90);
}
void loop() {
  Serial.println(myservo3.read());
  char x = Serial.read();
  if(x=='r'){ 
    handsUP1();
  }
  else if(x=='f'){
    handsDOWN1();
  }
  else if(x=='t'){
    handsUP2();
  }
  else if(x=='g'){
    handsDOWN2();
  }
  else if(x=='y'){
    handsUP3();
  }
  else if(x=='h'){
    handsDOWN3();
  }
  else if(x=='u'){
    handsUP4();
  }
  else if(x=='j'){
    handsDOWN4();
  }
  else if(x=='o'){
    handsUP1();
    delay(500);
    handsUP2();
    delay(500);
    handsDOWN1();
    delay(500);
    handsDOWN2(); 
    delay(500);
    handsUP3();
    delay(500);
    handsUP4();
    delay(500);
    handsDOWN3();
    delay(500);
    handsDOWN4(); 
  }
  delay(100);
}



/////////////////////////////
void handsUP1(){
    myservo4.write(170);
}

void handsDOWN1(){
    myservo4.write(90);
}
void handsUP2(){
    myservo5.write(150);              // tell servo to go to position in variable 'pos'
}

void handsDOWN2(){
    myservo5.write(90);              // tell servo to go to position in variable 'pos'
}

void handsUP3(){
    myservo2.write(10);   
}

void handsDOWN3(){
    myservo2.write(90);   
}


void handsUP4(){
    myservo3.write(100);              // tell servo to go to position in variable 'pos'
}

void handsDOWN4(){
      myservo3.write(170); 
}
