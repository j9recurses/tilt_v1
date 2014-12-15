// 1 = user
// 2 = caretaker

int user_fsrPin = A0;
int user_buzzerPin = 13;
int care_fsrPin = A5;   
int care_buzzerPin = 12;

int user_lastReading = 0;
int care_lastReading = 0;
int readSerial = 0;
int user_fsrVal = 0;
int care_fsrVal = 0;

void setup () {
  pinMode(user_fsrPin, INPUT);
  pinMode(care_fsrPin, INPUT);
  pinMode(user_buzzerPin, OUTPUT);
  pinMode(care_buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop () {
  // read fsr value and write to serial port
  user_fsrVal = analogRead(user_fsrPin);
  if (user_fsrVal > 10 && user_lastReading != 1) {
    Serial.println(1);
  }
  if (user_fsrVal > 10) {user_lastReading = 1; delay(500);}
  
  else {user_lastReading = 0;}
  
  care_fsrVal = analogRead(care_fsrPin);
  if (care_fsrVal > 10 && care_lastReading != 2) {
    Serial.println(2);
  }
  if (care_fsrVal > 10) {care_lastReading = 2; delay(500);}
  
  else {care_lastReading = 0;}
  
  // listen to serial port and and write to buzzer
  if (Serial.available() > 0) {
    readSerial = Serial.parseInt();
    if (readSerial == 1) {
      digitalWrite(care_buzzerPin, HIGH);
      delay(200);
      digitalWrite(care_buzzerPin, LOW);
    }
    if (readSerial == 2) {
      digitalWrite(user_buzzerPin, HIGH);
      delay(200);
      digitalWrite(user_buzzerPin, LOW);
    }
  }
}


