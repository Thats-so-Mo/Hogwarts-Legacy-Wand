# Casting Spells in Hogwarts Legacy (PC Only) with the Kano Wand and a Raspberry Pi Zero W

The basic idea behind this project is to convert the gestures/movements of the wand into keyboard button presses with the help of a Raspberry Pi Zero W. The wand connects to the RPI Zero W via Bluetooth which then RPI Zero W sends data to the PC with Hogwarts Legacy running on it via [USB (usb data port)](https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/).

This uses GammaGames' Kano_wand module/code (https://github.com/GammaGames/kano_wand) and I have a copy of their code/module included within my repository as a 
way to make it easier for people to clone. He has two repositories dedicated to the kano wand;https://github.com/GammaGames/kano_wand and https://github.com/GammaGames/kano-wand-demos (PLEASE CHECK THEM OUT). Without him, I would not have been possible to actually do this. Special Thanks to him, Jesse Linburg.

I also utilised this tutorial to setup and aided in the creation of my Hogwarts Legacy Wand code, [Maspieljr's instructable](https://www.instructables.com/SmartWand) is what I have followed to help set me up. The tutorial on the instructable is sourced from [Jesse Linburg (aka GammaGames) himself](https://medium.com/@gammagames/control-a-phillips-hue-bulb-with-the-flick-of-a-wand-3a9af4826775). Thanks to Maspieljr!

For the PC to accept commands from a wand, the Raspberry Pi Zero W is turned into a USB HID device, Special Thanks to RandomNerdTutorials [for this tutorial](https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/)

Special Thanks to the Harry Potter Nerds who filled out those wikias with wand movements, without them I wouldn't have know how to do an Accio cast. lol

Down below is just a slightly modified copy of the tutorial found on his Instructable and from the [original source material](https://medium.com/@gammagames/control-a-phillips-hue-bulb-with-the-flick-of-a-wand-3a9af4826775)

## First thing:  SETUP the RPI for Hogwarts Legacy Wand (Kano Wand). 

I essentially set up my RPI to be headless (You can find [tutorials online](https://www.tomshardware.com/how-to/set-up-raspberry-pi) for this). Found below, is the slightly modified verison of the tutorial, slightly more update to date.

~~~
**Step 1: RPI OS installed on Raspberry Pi**

Once you've completed the install, Run the two bottom commands in terminal to ensure RPI is update to date.

> sudo apt-get update

> sudo apt-get upgrade


**Step 2: Install Python 3**

Python3 should already be installed. But just incase run the command: 
sudo apt install python3 

**Step 3: Install modules for Kano Wand**

In terminal:

> cd /usr/local/lib/python3.9/dist-packages

then

> git clone https://github.com/GammaGames/kano_wand.git

> sudo pip3 install bluepy moosegesture

Had to use sudo for these to get the proper permissions. Also had to use the following commands instead to install numpy, for whatever reason, couldn't get pip to work. Might have been another path issue, but this worked for me so I went with it:

> sudo apt-get install python3-numpy

**Step 4: Clone the Hogwarts Legacy Wand repository**

Find a place where you want to clone the respository to, I essentially did it in my "Downloads" folder. So to return to home, type and enter:

> cd

then 

> cd Downloads

> sudo apt install git

> git clone https://github.com/Thats-so-Mo/Hogwarts-Legacy-Wand.git

> git clone https://github.com/GammaGames/kano_wand.git


~~~

## Second thing: Turn the Raspberry Pi Zero W into a USB HID Device

Now you have Hogwarts Legacy Wand downloaded but its not ready to be used as you need to convert the RPI Zero W into a USB HID device; which can be easily done by following this [tutorial](https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/). This is so that it makes it possible for the wand gestures to emulate keyboard button presses. Follow it all the way to Step 4. If you want to ensure that it is functioning as USB HID device, complete step 4. Remember, you followed the tutorial to step 4, YOU MUST CONNECT THE USB CABLE IN THE DATA USB PORT TO THE USB PORT On the PC WITH HOGWARTS LEGACY RUNNING ON IT.

Once done, launch terminal;

> cd Downloads\Hogwarts-Legacy-Wand

> chmod +x Hogwarts_Legacy.py

> sudo ./Hogwarts_Legacy.py 

sudo is needed due to bluepy being a bit of #$@##@ (permission issues)... If its done all correctly, it should start showing "scanning" in terminal...

When casting a spell, hold down the button on the wand. Down below are wand gestures that can be currently found within Hogwarts Legacy Wand code.

## Third Thing: Wand Gestures - Add/modifying/Removing Wand Gestures


