from Action import Action
from Menu import Menu
from MP3Menu import MP3Menu

class MP3Action (Action):    
    menu = None
    def __init__ (self,menu):
        self.menu = menu
        self.selectable = 1
        self.label = ">MP3 Player"


    def do (self):
        self.menu.newMenu = MP3Menu()





