from LCDController import LCDController
from MPG123 import MPG123
from Menu import Menu
from BootMenu import BootMenu
from LEDManager import LEDManager
from StatusMenu import StatusMenu
from random import randrange
import time
import sys
import os

lcd = LCDController("/dev/ttyUSB0")
#lcd.reboot()
lcd.clearScreen()
lcd.setLed(0,100,0)
lcd.setLed(1,0,0)
lcd.setLed(2,0,0)
lcd.setLed(3,0,0)

newMenu = Menu()
menu = BootMenu()
newMenu = menu


def updateDisplay (lcd,menu):
    updateLeds(menu.getLeds())
    lcd.clearScreen()
    idx = 0
    lcd.clearScreen()
    for line in menu.getDisplay():
        lcd.sendText(idx,0,line)
        idx += 1
    return

def updateLeds (leds):
    idx = 0
    for led in leds:
        lcd.setLed(idx,led.getGreenLvl(),led.getRedLvl())
        idx += 1

    return

while 1:

    if menu.getMenu() != None: menu=menu.getMenu()
    if menu.updateDisplay()      : updateDisplay (lcd,menu)
    #if ledManager.hasUpdate()    : updateLeds(ledManager.leds)

    keyStats = lcd.scanKeys()
    if keyStats != None :        
        if ord(keyStats['released_since_last']) != 0  :
           menu.handleInput(int ( ord (keyStats['released_since_last']) ) )    
            
    time.sleep(0.005)







