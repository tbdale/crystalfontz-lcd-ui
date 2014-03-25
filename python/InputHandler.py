import Menu

class InputHandler:

    TOP    = 0x01
    OK     = 0x02
    STOP   = 0x04
    LEFT   = 0x08
    RIGHT  = 0x10
    BOTTOM = 0x20

    menu = None
    
    def __init__ (self,menu):
        self.menu = menu


    
        
