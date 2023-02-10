#include <Keyboard.h>                               //Including the keyboard library
#include <Mouse.h>                                  //Including the mouse library
#include <WiiChuck.h>

Accessory nunchuck;


void setup() {

	Serial.begin(115200);
	nunchuck.begin();
	if (nunchuck.type == Unknown) {
		nunchuck.type = NUNCHUCK;
	}
}

void loop() {

  nunchuck.readData();
 int xaxismap = map(nunchuck.getJoyX(), -240, 240, -1, 1);
 int yaxismap = map(nunchuck.getJoyY(), -240, 240, -1, 1);

if (nunchuck.getButtonZ())                   //Checking if the first switch has been pressed
  {
    Keyboard.write('c');                            //Sending the "A" character
    delay(50);
  }
if (nunchuck.getButtonZ())                   //Checking if the first switch has been pressed
  {
    Keyboard.write('f');                            //Sending the "A" character
    delay(50);
  }
if (xaxismap = -1);                   //Checking if the first switch has been pressed
  {
    Keyboard.write('a');                            //Sending the "A" character
    delay(50);
  } 
if (xaxismap = 1);                   //Checking if the first switch has been pressed
  {
    Keyboard.write('d');                            //Sending the "A" character
    delay(50);
  }    
}