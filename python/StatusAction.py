from Action import Action
from Menu import Menu
from StatusMenu import StatusMenu

class StatusAction (Action):    
    menu = None
    def __init__ (self,menu):
        self.menu = menu
        self.selectable = 1
        self.label = ">Status"


    def do (self):
        self.menu.newMenu = StatusMenu()





