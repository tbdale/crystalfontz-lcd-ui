from LEDManager import LEDManager

class Menu:
    """ Menu base class """
    TOP    = 0x01
    OK     = 0x02
    STOP   = 0x04
    LEFT   = 0x08
    RIGHT  = 0x10
    BOTTOM = 0x20

    selectedIndex = -1
    actions = []
    displayLines = []
    newMenu = None

    update = 0

    ledManager = LEDManager()


    def displayMenu (self):
        
        idx = 0
        self.displayLines = []
        for action in self.actions:
            if idx > 3 : break
            else :
                line = ""
                print "Appending '"+action.getLabel()+"' to displayLines array"
                if action.canSelect():
                    line = "%-17s%3s" % (action.getLabel(), self.isSelected(idx))
                else: line = action.getLabel()
                self.displayLines.append(line)
            idx += 1
        self.update = 1
        return

    def isSelected (self,idx):
        if self.selectedIndex == idx: return "(*)"
        else:return "( )"

    def updateDisplay (self):
        return self.update

    def getDisplay (self):
        self.ledManager.oneOn(0,100,0)
        self.update = 0
        return self.displayLines

    def navigate (self,key):
        selections = []
        idx = 0
        for action in self.actions:
            if action.canSelect() : selections.append(idx);
            idx += 1
        if len(selections) > 0:
            if key==self.TOP:
                self.selectedIndex -= 1
                if self.selectedIndex < 0: self.selectedIndex = 0

            if key==self.BOTTOM:
                self.selectedIndex += 1
                if self.selectedIndex > (len(selections) -1): self.selectedIndex = 0

            if key==self.OK and self.selectedIndex > 0:
                self.actions[self.selectedIndex].do()

        return

    def handleInput (self,key):
        pass

    def getMenu (self):
        return self.newMenu

    def getLeds (self):
        return self.ledManager.getLeds()
