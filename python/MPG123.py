import threading
import os
import sys
import time
from math import floor


class MPG123(threading.Thread):
    """
    Class that interfaces to the MPG123 MP3 player application
    Author: Brian Dale
    Date: May 10, 2007
    """

    STATE_STOPPED = 0x00
    STATE_PLAYING = 0x01
    STATE_PAUSED  = 0x02

    state = None
    playingTime   = ""
    remainingTime = ""
    playerSTDOUT = None
    playerSTDIN  = None
    running = 0
    remote = None


    def __init__ (self):

        threading.Thread.__init__(self)
        (self.playerSTDOUT, self.playerSTDIN) = os.popen2("/usr/local/bin/mpg123 -R")
        self.running = 1
        self.state = MPG123.STATE_STOPPED


    def run (self):
        lineCount = 0
        line = ""
        data=""
        packet = self.playerSTDIN.read(10)
        while self.running:
            
            lineCount+=1
            line += packet
            if line.count("\n") > 0 :
                data = line[0:line.find("\n")]
                try:
                    (dType,payload) = data.split(" ",1)
                    if dType=="@F":
                        (currentFrame,framesRemain,secs,secsRemain) = payload.split(" ")
                        self.playingTime = self.getTimeFormatted(secs)
                        self.remainingTime = self.getTimeFormatted(secsRemain)
                    line = line[line.find("\n")+1:]
                except:
                    print "Exception in MPG123.run()",sys.exc_info()[0]
                    self.playingTime = "EXCEPTION"
                    time.sleep(1)

            packet = self.playerSTDIN.read(10)
            
        self.sendToRemotePlayer("q")
        return None

    def stopPlaying (self):

        self.sendToRemotePlayer("s")
        self.state = MPG123.STATE_STOPPED
        return None

    def play (self,filePath):
        self.sendToRemotePlayer("l "+filePath)
        self.state = MPG123.STATE_PLAYING
        return None

    def getPlayingTime (self):

        return self.playingTime;

    def getRemainingTime (self):

        return self.remainingTime

    def getTimeFormatted (self, secs):

        mins = int(floor(float(secs)/60))
        secs2 = int(float(secs)-(mins*60))
        secsField = ""
        minsField = ""
        if secs2 < 10 : secsField = "0" + str (secs2)
        else : secsField = str(secs2) 
        if mins < 1 : minsField = "0"
        else : minsField = str(mins)
        
        return minsField + ":" + secsField

    def sendToRemotePlayer (self,cmd):
        try:
            self.playerSTDOUT.write(cmd+"\n")
            self.playerSTDOUT.flush()
        except:
            print "Exception calling MPG123.sendToRemotePlayer(%s)" % cmd
        return None

    def quit (self):
        self.stopPlaying()
        self.running = 0

        return None

    def getState (self):

        return self.state





