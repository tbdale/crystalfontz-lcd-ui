class LED:

    greenLvl = 0
    redLvl   = 0

    def __init__ (self,g=0,r=0):
        self.greenLvl = g
        self.redLvl   = r

    def getGreenLvl (self):
        return self.greenLvl

    def getRedLvl (self):
        return self.redLvl

    def setGreenLvl (self,v):
        self.greenLvl = v

    def setRedLvl (self,v):
        self.redLvl = v
