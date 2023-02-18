#!/usr/bin/env python3
#!Hogwarts Legacy Wand!
#This code is created/modified by 'That's So Mo', the code itself is a modified verison/based off of maspieljr (https://www.instructables.com/SmartWand/)
#This code uses the kano_wand library/module which was created by GammaGames (https://github.com/GammaGames/kano_wand)
#This code uses code that turns the RPI Zero to a USB HID device - I followed RandomNerdTutorials tutorial (https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/)
#Thanks to GammaGames, RandomNerdTutorials, maspieljr - without them, I wouldn't have been able to do this. Thank You. 
#And a special thanks to the Harry Potter fans who contribute so much to the wikias - helped fill in the blanks for some wand movements
#This code is opensource/free to use and modify etc.
#Check my YouTube Channel!: https://www.youtube.com/thatssomo1
#  _    _                                _         _                                  __          __             _ 
# | |  | |                              | |       | |                                 \ \        / /            | |
# | |__| | ___   __ ___      ____ _ _ __| |_ ___  | |     ___  __ _  __ _  ___ _   _   \ \  /\  / /_ _ _ __   __| |
# |  __  |/ _ \ / _` \ \ /\ / / _` | '__| __/ __| | |    / _ \/ _` |/ _` |/ __| | | |   \ \/  \/ / _` | '_ \ / _` |
# | |  | | (_) | (_| |\ V  V / (_| | |  | |_\__ \ | |___|  __/ (_| | (_| | (__| |_| |    \  /\  / (_| | | | | (_| |
# |_|  |_|\___/ \__, | \_/\_/ \__,_|_|   \__|___/ |______\___|\__, |\__,_|\___|\__, |     \/  \/ \__,_|_| |_|\__,_|
#                __/ |                                         __/ |            __/ |                              
#               |___/                                         |___/            |___/                               
#

from kano_wand.kano_wand import Shop, Wand, PATTERN
import moosegesture as mg
import sys
import time
import random


NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


#Wand Module classes and definitions
class GestureWand(Wand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Basic gesture dictionary
        # We use them as tuples so we can use them as keys
        self.gestures = {
            ("U", "U"): "lumos",
            ("D", "D"): "nox",
            ("DL", "R", "DL"): "stupefy",
            ("DR", "R", "UR", "D"): "wingardium_leviosa",
            ("DR", "R", "U"): "levioso",
            ("UL", "UR"): "reducio",
            ("DR", "U", "UR", "DR", "UR"): "flipendo",
            ("R", "D"): "expelliarmus",
            ("UR", "DR", "L"): "incendio",
            ("U", "D", "DR", "R", "L"): "locomotor",
            ("DR", "DL"): "engorgio",
            ("UR", "R", "DR"): "aguamenti",
            ("UR", "R", "DR", "UR", "R", "DR"): "avis",
            ("D", "R", "U"): "reducto",
            ("DR", "R", "UR", "UL", "UR", "R", "DR"): "reparo",
            ("DR", "R", "UR", "U", "UL"): "reparo",
            ("DR", "R", "UR", "UL", "L", "R"): "reparo",
            ("DR", "R", "UR", "UL", "UR", "R"): "reparo",
            ("DR", "R", "UR", "UL", "L", "UL", "R"): "reparo",
            ("DR", "R", "UR", "UL", "R", "DR"): "reparo",
            ("DR", "R", "UL", "L", "R", "D"): "reparo",
            ("U", "DR", "DL", "DR"): "revelio",
            ("DR", "UR"): "protego",
            ("UR", "R", "DR"): "accio",
            ("DR", "U", "DL"): "ancient",
            ("R", "L"): "basic",
            ("L", "R"): "basic",
            ("U", "DL", "U"): "changespells",
            ("UR", "R", "DR", "DL", "L", "UL", "UR", "R", "DR", "DL"): "disillusionment",
            ("R", "DL", "R"): "ancient_throw"
        }
        self.spell = None
        self.pressed = False
        self.positions = []

    def post_connect(self):
        self.subscribe_button()
        self.subscribe_position()

    def on_position(self, x, y, pitch, roll):
        if self.pressed:
            # While holding the button,
            #   append the position to the positions array
            self.positions.append(tuple([x, -1 * y]))

    def on_button(self, pressed):
        self.pressed = pressed

        if pressed:
            self.spell = None
        else:
            # If releasing the button, get the gesture
            gesture = mg.getGesture(self.positions)
            self.positions = []
            closest = mg.findClosestMatchingGesture(gesture, self.gestures, maxDifference=1)

            if closest != None:
                # Just use the first gesture in the list using the gesture key
                self.spell = self.gestures[closest[0]]
                self.vibrate(PATTERN.SHORT)
            # Print out the gesture
            print("{}: {}".format(gesture, self.spell))


def main():
    # Create the manager and shop to search for wands
    shop = Shop(wand_class=GestureWand)
    wands = []

    try:
        # Scan for wands until it finds one
        while len(wands) == 0:
            print("Scanning...")
            wands = shop.scan(connect=True)

        wand = wands[0]
        while wand.connected:
            # Make a random sleep and transition time
            sleep = random.uniform(0.1, 0.2)
#            transition = math.ceil(sleep * 10)
            if wand.spell == "protego":
                print('protego spell detected')
                write_report(NULL_CHAR*2+chr(20)+NULL_CHAR*5) #press letter q
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "changespells":
                print('changle spells detected')
                write_report(NULL_CHAR*2+chr(54)+NULL_CHAR*5) #press letter ,
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "ancient":
                print('ancient spell detected')
                write_report(NULL_CHAR*2+chr(27)+NULL_CHAR*5) #press letter x
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "revelio":
                print('revelio spell detected')
                write_report(NULL_CHAR*2+chr(21)+NULL_CHAR*5) #press letter r
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "basic":
                print('basic spell detected')
                write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5) #press letter b
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "ancient_throw":
                print('ancient_throw spell detected')
                write_report(NULL_CHAR*2+chr(29)+NULL_CHAR*5) #press letter z
                write_report(NULL_CHAR*8)
                wand.spell = None
            #LEVEL 1 - FIRST ROW OF SPELLS
            if wand.spell == "expelliarmus":
                print('expelliarmus spell detected')
                write_report(NULL_CHAR*2+chr(30)+NULL_CHAR*5) #press number 1
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "incendio":
                print('incendio spell detected')
                write_report(NULL_CHAR*2+chr(31)+NULL_CHAR*5) #press number 2
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "levioso":
                print('levioso spell detected')
                write_report(NULL_CHAR*2+chr(32)+NULL_CHAR*5) #press number 3
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "accio":
                print('accio spell detected')
                write_report(NULL_CHAR*2+chr(33)+NULL_CHAR*5) #press number 4
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            #LEVEL 2 -SECOND ROW OF SPELLS
            if wand.spell == "lumos":
                print('lumos spell detected')
                write_report(NULL_CHAR*2+chr(30)+NULL_CHAR*5) #press number 1
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "nox":
                write_report(NULL_CHAR*2+chr(30)+NULL_CHAR*5)
                # Release keys
                write_report(NULL_CHAR*8)  #press number 1
                wand.spell = None
            if wand.spell == "disillusionment":
                print('dissillusionment charm detected')
                write_report(NULL_CHAR*2+chr(31)+NULL_CHAR*5) #press number 2
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "reparo":
                print('reparo spell detected')
                write_report(NULL_CHAR*2+chr(32)+NULL_CHAR*5) #press number 3
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "accio":
                print('accio spell detected')
                write_report(NULL_CHAR*2+chr(33)+NULL_CHAR*5) #press number 3
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            #LEVEL 3 - THIRD ROW OF SPELLS
            if wand.spell == "lumos":
                print('lumos spell detected')
                write_report(NULL_CHAR*2+chr(30)+NULL_CHAR*5) #press number 1
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "nox":
                write_report(NULL_CHAR*2+chr(31)+NULL_CHAR*5)
                # Release keys
                write_report(NULL_CHAR*8)  #press number 1
                wand.spell = None
            if wand.spell == "incendio":
                print('incendio spell detected')
                write_report(NULL_CHAR*2+chr(32)+NULL_CHAR*5) #press number 2
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "reparo":
                print('reparo spell detected')
                write_report(NULL_CHAR*2+chr(33)+NULL_CHAR*5) #press number 3
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            #LEVEL 4 -Fourth ROW OF SPELLS
            if wand.spell == "lumos":
                print('lumos spell detected')
                write_report(NULL_CHAR*2+chr(30)+NULL_CHAR*5) #press number 1
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "nox":
                write_report(NULL_CHAR*2+chr(31)+NULL_CHAR*5)
                # Release keys
                write_report(NULL_CHAR*8)  #press number 1
                wand.spell = None
            if wand.spell == "incendio":
                print('incendio spell detected')
                write_report(NULL_CHAR*2+chr(32)+NULL_CHAR*5) #press number 2
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            if wand.spell == "reparo":
                print('reparo spell detected')
                write_report(NULL_CHAR*2+chr(33)+NULL_CHAR*5) #press number 3
                # Release keys
                write_report(NULL_CHAR*8)
                wand.spell = None
            time.sleep(sleep)

#    # Detect keyboard interrupt and disconnect wands,
    except KeyboardInterrupt as e:
        for wand in wands:
            wand.disconnect()
#        manager.reset()


if __name__ == "__main__":
    main()
