# Hogwarts-Legacy-Wand
### Use the Kano Wand for Hogwarts Legacy (PC Only)

The basic idea behind this project is to convert the gestures/movements of the wand into keyboard button presses.

This uses GammaGames' Kano_wand module/code (https://github.com/GammaGames/kano_wand) and I have a copy of their code/module included within my respiority as a 
way to make it easier for people to clone. He has two respositories dedicated to the kano wand;https://github.com/GammaGames/kano_wand and https://github.com/GammaGames/kano-wand-demos (PLEASE CHECK THEM OUT).
I also utilise this tutorial to setup and help me write the code, written by maspieljr, Here is his instructable that I have followed: https://www.instructables.com/SmartWand/ - turns out maspieljr got it from https://medium.com/@gammagames/control-a-phillips-hue-bulb-with-the-flick-of-a-wand-3a9af4826775


First step in SETUP is https://www.instructables.com/SmartWand/

~~~
Step 1: Install RPI OS on Raspberry Pi

Once you've complete the install and have a Linux Command Prompt, it's good practice to run the following two commands to be sure everything is up to date.

sudo apt-get update

sudo apt-get upgrade

Type the following at the command line interface to launch the desktop UI.

sudo startx


Step 2: Install Python 3

Python3 should already be installed with Raspian Stretch.

Follow this guide created by GammaGames

https://medium.com/@jesse007.gg/control-a-phillips...

I first had to change to a different directory before cloning the kano_wand repo, otherwise my python script couldn't find it. Probably could have updated some path references in some file somewhere, but I didn't dig into that.

cd /usr/local/lib/python3.5/dist-packages

git clone  <a href="https://github.com/GammaGames/kano_wand.git" rel="nofollow"> https://github.com/GammaGames/kano_wand.git</a>

sudo pip3 install bluepy moosegesture

Had to use sudo for these to get the proper permissions. Also had to use the following commands instead to install numpy, for whatever reason, couldn't get pip to work. Might have been another path issue, but this worked for me so I went with it:

sudo apt-get install python3-numpy
~~~
