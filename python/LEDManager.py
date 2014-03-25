from random import randrange

from LED import LED

class LEDManager:
    update = 0
    currentState = 0
    leds = []
    def __init__ (self):
        self.leds = []
        self.leds.append(LED(0,0))
        self.leds.append(LED(0,0))
        self.leds.append(LED(0,0))
        self.leds.append(LED(0,0))

    def oneOn (self,idx,greenLvl,redLvl):
        i = 0
        for led in self.leds :
            if i == idx : self.leds[i] = LED(greenLvl,redLvl)
            else        : self.leds[i] = LED(0,0)
        self.update = 1

    def randomizer (self):
        self.leds[0].setGreenLvl(randrange(0,100))
        self.leds[0].setRedLvl(randrange(0,100))

        self.leds[1].setGreenLvl(randrange(0,100))
        self.leds[1].setRedLvl(randrange(0,100))

        self.leds[2].setGreenLvl(randrange(0,100))
        self.leds[2].setRedLvl(randrange(0,100))

        self.leds[3].setGreenLvl(randrange(0,100))
        self.leds[3].setRedLvl(randrange(0,100))

        self.update = 1

        return

    def getLeds (self):
        return self.leds


    def hasUpdate (self):
        retval = self.update
        self.update = 0
        return retval


