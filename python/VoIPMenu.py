from Menu import Menu
from Action import Action
from VoIPCallAction import VoIPCallAction
import TopMenu
from os import popen2

class VoIPMenu(Menu):
    actions = []
    prevMenu = None
    def __init__ (self):
        self.actions = []
        self.displayLines = []
        self.displayLines.append("- Place VoIP Call -".center(20))
        self.actions.append(VoIPCallAction(self,"Cell","9195551212"))
        self.actions.append(Action(""))
        self.actions.append(Action(""))
        self.actions.append(Action(""))
        self.displayMenu()

    def handleInput (self,key):
        if key == self.STOP:
            popen2("/etc/init.d/asterisk stop")
            self.newMenu = TopMenu.TopMenu()
        else: 
            selections = []
            idx = 0
            for action in self.actions:
                if action.canSelect() : 
                    print "idx="+str(idx)+","+action.getLabel()+" can be selected"
                    selections.append(idx);
                idx += 1
            if len(selections) > 0:
                if key==self.TOP:
                    self.selectedIndex = self.selectedIndex - 1
                    if self.selectedIndex < 0: self.selectedIndex = 0
                    print "Selected index="+str(self.selectedIndex)
                    self.displayMenu()
    
                if key==self.BOTTOM:
                    self.selectedIndex += 1
                    if self.selectedIndex > (len(selections) -1): self.selectedIndex = 0
                    print "Selected index="+str(self.selectedIndex)
                    self.displayMenu()
    
                if key==self.OK and self.selectedIndex > -1:
                    self.actions[self.selectedIndex].do()
