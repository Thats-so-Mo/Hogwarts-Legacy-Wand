# Hogwarts-Legacy-Wand
### Use the Kano Wand for Hogwarts Legacy (PC Only)

The basic idea behind this project is to convert the gestures/movements of the wand into keyboard button presses with the help of a Raspberry Pi Zero.

This uses GammaGames' Kano_wand module/code (https://github.com/GammaGames/kano_wand) and I have a copy of their code/module included within my repository as a 
way to make it easier for people to clone. He has two repositories dedicated to the kano wand;https://github.com/GammaGames/kano_wand and https://github.com/GammaGames/kano-wand-demos (PLEASE CHECK THEM OUT). Without him, I would not have been possible to actually do this.

I also utilised this tutorial to setup and aided in the creation of my Hogwarts Legacy Wand code, [Maspieljr's instructable](https://www.instructables.com/SmartWand) is what I have followed to help set me up. The tutorial on the instructable is sourced from [Jesse Linburg (aka GammaGames) himself](https://medium.com/@gammagames/control-a-phillips-hue-bulb-with-the-flick-of-a-wand-3a9af4826775). 

Down below is just a slightly modified copy of the tutorial found on his Instructable and from the [original source material](https://medium.com/@gammagames/control-a-phillips-hue-bulb-with-the-flick-of-a-wand-3a9af4826775)

First thing you got to do is to SETUP the RPI for Hogwarts Legacy Wand. I essentially set up my RPI to be headless (You can find [tutorials online](https://www.tomshardware.com/how-to/set-up-raspberry-pi) for this). Found below, is the slightly modified verison of the tutorial, slightly more update to date.

~~~
Step 1: RPI OS installed on Raspberry Pi

Once you've completed the install, Run the two bottom commands in terminal to ensure RPI is update to date.

> sudo apt-get update

> sudo apt-get upgrade


Step 2: Install Python 3

Python3 should already be installed. But just incase run the command: 
sudo apt install python3 

Step 3: Install modules for Kano Wand

In terminal:

> cd /usr/local/lib/python3.9/dist-packages

then

> git clone https://github.com/GammaGames/kano_wand.git

> sudo pip3 install bluepy moosegesture

Had to use sudo for these to get the proper permissions. Also had to use the following commands instead to install numpy, for whatever reason, couldn't get pip to work. Might have been another path issue, but this worked for me so I went with it:

> sudo apt-get install python3-numpy
~~~
