from LCDController import LCDController
from random import randrange
import time
import sys

lcd = LCDController("/dev/ttyUSB0")

print lcd.getFirmware()
lcd.reboot()

