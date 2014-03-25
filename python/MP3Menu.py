from Menu import Menu
from Action import Action
from MPG123 import MPG123
import os
from os import popen2
from string import strip

import time

import TopMenu

class MP3Menu(Menu):
    mpgPlayer = None
    fileList = []
    MP3DIR = "/mp3/"

    STOPPED = 0
    PLAYING = 1

    STATE =  STOPPED

    SCROLLIDX = 0
    SCROLLDIR = 0

    currentFIleIdx = 0

    def __init__ (self):
        self.displayLines = []
        self.displayLines.append(">>>>MP3 Player<<<<".center(20))
        self.displayLines.append("Playing:")
        self.displayLines.append("")
        self.displayLines.append("")
        self.update = 1
        self.scanDir();
        self.displayLines[1]="- Playing -".center(20)        
        self.update = 1
        self.mpgPlayer = MPG123()
        self.mpgPlayer.start()
        self.mpgPlayer.play(self.fileList[self.currentFIleIdx])
        self.STATE = self.PLAYING

    def scanDir (self):
        si,so = popen2("/usr/bin/find " + self.MP3DIR + " -type f -iname *.mp3")
        for line in so:
            print "Adding" + strip(line)
            self.fileList.append( strip(line ) )

    def updateDisplay (self):
        if self.STATE == self.PLAYING:
            if self.mpgPlayer.getPlayingTime() == "EXCEPTION":
                self.mpgPlayer.quit()
                os.system("killall -9 mpg123")
                self.mpgPlayer = MPG123()
                self.mpgPlayer.start()
                self.mpgPlayer.play(self.fileList[self.currentFIleIdx])

            self.ledManager.randomizer()
            self.displayLines[2] = self.lineScroll( (self.fileList[self.currentFIleIdx])[len(self.MP3DIR):] )
            self.displayLines[3] = ( self.mpgPlayer.getPlayingTime()+"/"+self.mpgPlayer.getRemainingTime() ).center(20)
            if self.mpgPlayer.getRemainingTime() == "0:00":
                time.sleep(0.1)
                self.playNext()
        return 1

    def displayMenu (self):
        
        idx = 0
        
        self.update = 1
        return

    def lineScroll (self,s):
        if len(s) < 21: return s

        
        if self.SCROLLDIR == 0:
            if (len(s) - self.SCROLLIDX) < 19 :
                self.SCROLLDIR = 1                
            else:
                self.SCROLLIDX += 1

        if self.SCROLLDIR == 1:
            if  self.SCROLLIDX < 1 :
                self.SCROLLIDX = 0
                self.SCROLLDIR = 0                
            else:
                self.SCROLLIDX -= 1

        s =  (s[self.SCROLLIDX:])[:20]
        print "Returning " + s

        return s


    def playPrev (self):
        self.SCROLLIDX = 0
        self.SCROLLDIR = 0
        self.mpgPlayer.stopPlaying()
        self.STATE = self.STOPPED
        self.currentFIleIdx = self.currentFIleIdx - 1
        if self.currentFIleIdx < 0: self.currentFIleIdx = len(self.fileList) -1
        print "Selected fileIdx="+str(self.currentFIleIdx)
        self.displayLines[1]="- Playing -".center(20)
        self.displayLines[2]=((self.fileList[0])[len(self.MP3DIR):])[:20]
        self.mpgPlayer.play(self.fileList[self.currentFIleIdx])
        self.STATE = self.PLAYING

        return

    def playNext (self):
        self.SCROLLIDX = 0
        self.SCROLLDIR = 0
        self.mpgPlayer.stopPlaying()
        self.STATE = self.STOPPED
        self.currentFIleIdx = self.currentFIleIdx + 1
        if self.currentFIleIdx > len(self.fileList) -1: self.currentFIleIdx = 0
        print "Selected fileIdx="+str(self.currentFIleIdx)
        self.displayLines[1]="- Playing -".center(20)
        self.displayLines[2]=((self.fileList[self.currentFIleIdx])[len(self.MP3DIR):])[:20]        
        self.mpgPlayer.play(self.fileList[self.currentFIleIdx])
        self.STATE = self.PLAYING

        return


    def handleInput (self,key):
        if key==self.STOP and self.STATE == self.STOPPED:
            self.mpgPlayer.quit()
            self.newMenu = TopMenu.TopMenu()
        if key==self.OK and self.STATE == self.STOPPED:
            self.displayLines[1]="- Playing -".center(20)
            self.displayLines[2]=((self.fileList[self.currentFIleIdx])[len(self.MP3DIR):])[:20]        
            self.mpgPlayer.play(self.fileList[self.currentFIleIdx])
            self.STATE = self.PLAYING
        else: 
      
            if key==self.LEFT:
                self.playPrev()                
                
            if key==self.RIGHT:
                self.playNext()

            if key==self.STOP :
                self.mpgPlayer.quit()
                self.displayLines[1]="- Stopped -".center(20)
                self.STATE = self.STOPPED

            if key==self.STOP :
                self.mpgPlayer.quit()
                self.displayLines[1]="- Stopped -".center(20)
                self.STATE = self.STOPPED

        def getLeds (self):
            self.ledManager.randomizer()
            return self.ledManager.getLeds()    
        #if mpgPlayer.getState() == MPG123.STATE_PLAYING : mpgPlayer.stopPlaying()
        #if mpgPlayer.getState() == MPG123.STATE_STOPPED : mpgPlayer.play()
        
