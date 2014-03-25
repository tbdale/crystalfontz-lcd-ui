from Action import Action
from TopMenu import TopMenu

class BootMenuAction (Action):
    
    def __init__ (self,label):
        self.label = label       

    def do (self):
        self.menu = TopMenu()
