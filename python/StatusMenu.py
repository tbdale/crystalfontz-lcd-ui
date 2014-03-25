from Menu import Menu
from Action import Action
import TopMenu

class StatusMenu(Menu):
    actions = []
    prevMenu = None
    def __init__ (self):
        self.actions = []
        self.actions.append(Action(">OpenVPN : OK"))
        self.actions.append(Action(">WiFi    : OK"))
        self.actions.append(Action(">VoIP    : OK"))
        self.actions.append(Action(""))
        self.displayMenu()

    def handleInput (self,key):
        self.newMenu = TopMenu.TopMenu()
