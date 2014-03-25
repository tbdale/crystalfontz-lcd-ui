from Menu import Menu
from BootMenuAction import BootMenuAction
from TopMenu import TopMenu

class BootMenu (Menu):
           
    def __init__ (self):
        self.actions = []
        self.ledManager.oneOn(0,100,0)
        self.actions.append(BootMenuAction(">>>MP3/WiFi/VoIP<<<"))
        self.actions.append(BootMenuAction("Ready:"))
        self.actions.append(BootMenuAction("(2008)".center(20)))
        self.actions.append(BootMenuAction("Brian Dale".center(20)))
        self.displayMenu()
    
    def handleInput (self,key):
        self.newMenu = TopMenu()


