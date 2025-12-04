//ArduinoSNESController.ino
//SHIFT REGISTER EDITION
//Version 1.1 (July 28, 2015)
//For Arduino Mega 1200
//See r.lagserv.net for directions
//By Riley Johanson 
#define aPin 11
#define bPin 10
#define xPin 9
#define yPin 8
#define lPin 7
#define rPin 6
#define leftPin 5
#define rightPin 4
#define upPin 3
#define downPin 2
#define startPin 0
#define selectPin 1 

void setup() {
  // put your setup code here
  pinMode(aPin, OUTPUT);        //A button                'a'
  pinMode(bPin, OUTPUT);        //B button                'b'
  pinMode(xPin, OUTPUT);        //X button                'x'
  pinMode(yPin, OUTPUT);        //Y button                'y'
  pinMode(lPin, OUTPUT);        //Left shoulder button;   'q'
  pinMode(rPin, OUTPUT);        //Right shoulder button   'w'
  pinMode(leftPin, OUTPUT);     //Left DPad button        'l'
  pinMode(rightPin, OUTPUT);    //Right DPad button       'r'
  pinMode(upPin, OUTPUT);       //Up DPad button          'u'
  pinMode(downPin, OUTPUT);     //Down DPad button        'd'
  pinMode(startPin, OUTPUT);    //Start button            's'
  pinMode(selectPin, OUTPUT);   //Select button           'z'

  digitalWrite(aPin, HIGH);        //A button                'a'
  digitalWrite(bPin, HIGH);        //B button                'b'
  digitalWrite(xPin, HIGH);        //X button                'x'
  digitalWrite(yPin, HIGH);        //Y button                'y'
  digitalWrite(lPin, HIGH);        //Left shoulder button;   'q'
  digitalWrite(rPin, HIGH);        //Right shoulder button   'w'
  digitalWrite(leftPin, HIGH);     //Left DPad button        'l'
  digitalWrite(rightPin, HIGH);    //Right DPad button       'r'
  digitalWrite(upPin, HIGH);       //Up DPad button          'u'
  digitalWrite(downPin, HIGH);     //Down DPad button        'd'
  digitalWrite(startPin, HIGH);    //Start button            's'
  digitalWrite(selectPin, HIGH);   //Select button           'z'
  
  Serial.begin(9600);
}

void loop() {
  int cmd;

  cmd = Serial.read();
  
  //Serial.write(cmd);        // Echo exactly what was received
  switch(cmd)
  {
    case 'A': { pressButton(aPin);        break; }
    case '1': { releaseButton(aPin);      break; }
    case 'B': { pressButton(bPin);        break; }
    case '2': {releaseButton(bPin);       break; }
    case 'X': { pressButton(xPin);        break; }
    case '4': { releaseButton(xPin);      break; }
    case 'Y': { pressButton(yPin);        break; }
    case '3': { releaseButton(yPin);      break; }
    case 'L': { pressButton(leftPin);     break; }
    case '5': { releaseButton(leftPin);   break; }
    case 'R': { pressButton(rightPin);    break; }
    case '6': { releaseButton(rightPin);  break; }
    case 'U': { pressButton(upPin);       break; }
    case '7': { releaseButton(upPin);     break; }
    case 'D': { pressButton(downPin);     break; }
    case '8': { releaseButton(downPin);   break; }
    case 'Q': { pressButton(lPin);        break; }
    case 'O': { releaseButton(lPin);      break; }
    case 'W': { pressButton(rPin);        break; }
    case 'I': { releaseButton(rPin);      break; }
    case 'S': { pressButton(startPin);    break; }
    case '9': { releaseButton(startPin);  break; }
    case 'Z': { pressButton(selectPin);   break; }
    case 'P': { releaseButton(selectPin); break; }       
  }
}

void pressButton(int button)
{
  digitalWrite(button, LOW);
  delay(10);
}

void releaseButton(int button)
{
  digitalWrite(button, HIGH);
  delay(10);
}
