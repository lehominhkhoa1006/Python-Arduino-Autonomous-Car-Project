#include <AFMotor.h>

AF_DCMotor motor1(1); // Declare motor1 at pin 1 of Shield
AF_DCMotor motor2(2); // Declare motor2 at pin 2 of Shield
AF_DCMotor motor3(3); // Declare motor3 at pin 3 of Shield
AF_DCMotor motor4(4); // Declare motor4 at pin 4 of Shield

bool goLeftActive = false;
bool goRightActive = false;
int goLeftCount = 0;
int goRightCount = 0;

void setup() {
  Serial.begin(115200); // Start Serial communication with a baud rate of 115200
  // Start the motors
  motor1.setSpeed(255); // Set speed (range from 0 to 255)
  motor2.setSpeed(255);
  motor3.setSpeed(255);
  motor4.setSpeed(255);
}

void loop() {
  if (Serial.available() > 0) {
    // Read data from Serial
    char command = Serial.read();
    // Control motors based on data received from Python
    if (command == 'S') {
      // Run all motors at maximum speed, but the direction of rotation is BACKWARD instead of FORWARD
      motor1.run(BACKWARD);
      motor2.run(BACKWARD);
      motor3.run(BACKWARD);
      motor4.run(BACKWARD);
      // Reset counter and status variables
      goLeftActive = false;
      goRightActive = false;
      goLeftCount = 0;
      goRightCount = 0;
    } else if (command == 'F') {
      // Run all motors at maximum speed
      motor1.run(FORWARD);
      motor2.run(FORWARD);
      motor3.run(FORWARD);
      motor4.run(FORWARD);
      // Reset counter and status variables
      goLeftActive = false;
      goRightActive = false;
      goLeftCount = 0;
      goRightCount = 0;
    } else if (command == 'L') {
      // Pause motor 1 and motor 3 if not already paused
      if (!goLeftActive) {
        motor1.run(RELEASE);
        motor3.run(RELEASE);
        goLeftActive = true;
      }
      goLeftCount++;
    } else if (command == 'R') {
      // Pause motor 2 and motor 4 if not already paused
      if (!goRightActive) {
        motor2.run(RELEASE);
        motor4.run(RELEASE);
        goRightActive = true;
      }
      goRightCount++;
    }

    // Check if Python has stopped sending the "Go left" signal
    if (goLeftActive && command != 'L') {
      goLeftActive = false;
      // Reactivate motor 1 and motor 3 if the "Go left" signal has been received enough times
      if (goLeftCount >= 3) {
        motor1.run(FORWARD);
        motor3.run(FORWARD);
        goLeftCount = 0;
      }
    }

    // Check if Python has stopped sending the "Go right" signal
    if (goRightActive && command != 'R') {
      goRightActive = false;
      // Reactivate motor 2 and motor 4 if the "Go right" signal has been received enough times.
      if (goRightCount >= 3) {
        motor2.run(FORWARD);
        motor4.run(FORWARD);
        goRightCount = 0;
      }
    }
  }
}

