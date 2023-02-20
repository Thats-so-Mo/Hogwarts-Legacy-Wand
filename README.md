# Casting Spells in Hogwarts Legacy (PC Only) with the Kano Wand and a Raspberry Pi Zero W

The basic idea behind this project is to convert the gestures/movements of the wand into keyboard button presses with the help of a Raspberry Pi Zero W. The wand connects to the RPI Zero W via Bluetooth which then RPI Zero W sends data to the PC with Hogwarts Legacy running on it via [USB (usb data port)](https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/).

##Check out the video for a demonstration and setup

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/V1tuf1zIyzc/0.jpg)](https://youtu.be/V1tuf1zIyzc)

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

In the "class GestureWand(Wand)" sectopm, under the self gestures part. This is where you put in the gestures/spells you want to be able to perform. Some have been pulled by GammaGames and put in such as lumos where as I put in the accio, reparo, revelio and etc by using existing information available on their wand movements looking around online, on certain wikis or even on the kano wand spell sheet however for ancient spell and ancient throw spell, basic spell, etc - i just made it up. 

For example, ancient throw spell is just me tracing the letter Z in the air with the wand - Z being the letter to press for ancient spell in Hogwarts Legacy by default.

But if you want to insert accurate gestures and wand movements - use GammaGames gesture script, trace the spell with the wand and it displays the corresponding movement and then just copy and paste it into my script and give it a name. There are 8 different directions that the wand can detect; Up, Down, Left, Right, Up left, Up Right, Down Left, Down Right.. Flick the wand up - you get a U… you get the gist. Do a bunch of wand movements, it translates those movements in those 8 directions and then spits out the movements you did with the wand. Pretty simple - works great and surprisingly accurate. If you want to add your own spell, just copy the format of another spell or rewrite an existing one (e.g. reparo, Idk why i have so many) and then bobs your uncle.

Now in the "def main():" section

We get a bunch of "ifwand spell" commands.

The first you see are the default spells such as Protego (which is the letter 'Q'), revelio (letter 'R') and basic spell being the letter 'B'. With basic spell, I did set that up in Hogwarts Legacy to be the letter 'B'.

Using protego as an example,

When the script detects the protego spell casted by the wand, it will first print [protego spell detected] and then send the corresponding key press to the pc which in this case is the letter 'q' (write_report(NULL_CHAR*2+chr(20)+NULL_CHAR*5)).

Then it releases the “keyboard” (write_report(NULL_CHAR*8)) - without this line. It will pretty much spam the letter ''

"write_report(NULL_CHAR*2+chr(20)+NULL_CHAR*5)" 

The "20" value is the decimal value of 'Q'. if your protego is actually the letter M, you use the Univerisal Serial bus hid usage table (https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf), scroll down to Table 12 of the document to find its corresponding value and replace number 20 with the number 16 (From Table 12)
- Thats it - no other changes are needed

Now, if you want to change a spell, lets say in row 1, spell number 1, all you need to do is change expellarimus to another spell such as wingardium_levisa and thats pretty much it….

Now I know this method, this code, isnt perfect. When the spells have been chosen, with each number and row associated for each spell. This makes it so that there are 4 different wand gestures, four spells that can trigger a button press

For example with number 2, 

There are four spells that can trigger number 2; incendio, disillusionment, flipendo and windgardium leviosa. If your in the wrong row such as the first row but you do the wand gesture for windgardium leviosa, it will trigger incendio. So its up to the player to remain vigilant. I have so far set myself up that the first row are the spells that I want to use during battle while the other rows could be used for different utilities such as conjuring.

