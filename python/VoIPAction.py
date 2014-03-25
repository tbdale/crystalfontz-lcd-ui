from Action import Action
from VoIPMenu import VoIPMenu

class VoIPAction (Action):    
    menu = None
    def __init__ (self,menu):
        self.menu = menu
        self.selectable = 1
        self.label = ">VoIP"


    def do (self):
        self.menu.newMenu = VoIPMenu()





