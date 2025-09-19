const int SWITCH_PIN = 9;
const int X_PIN = A0;
const int Y_PIN = A1;

void setup() {
  pinMode(SWITCH_PIN, INPUT_PULLUP);
  pinMode(X_PIN, INPUT);
  pinMode(Y_PIN, INPUT);
  Serial.begin(115200);
}

void loop() {
  int xValue = analogRead(X_PIN);
  int yValue = analogRead(Y_PIN);
  int switchState = digitalRead(SWITCH_PIN);
  Serial.println("[MOUSE] " + String(xValue) + " " + String(yValue));
  Serial.println("[CLICK] " + String(switchState));
}
