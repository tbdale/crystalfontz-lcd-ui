from Menu import Menu
from Action import Action
import BootMenu
from StatusAction import StatusAction
from MP3Action import MP3Action
from VoIPAction import VoIPAction

class TopMenu(Menu):
    actions = []
    prevMenu = None
    def __init__ (self):
        self.actions = []
        self.actions.append(StatusAction(self))
        self.actions.append(MP3Action(self))
        self.actions.append(VoIPAction(self))
        self.actions.append(Action(""))
        
        self.displayMenu()

    def handleInput (self,key):
        if key==self.STOP: self.newMenu = BootMenu.BootMenu()
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

        return
