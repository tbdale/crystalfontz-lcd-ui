class Action:

    label = ""
    selectable = 0

    def __init__ (self,label="",s=0):
        self.label = label
        self.selectable = s

    def getLabel (self):
        return self.label

    def do (self):
        tmp = 1

    def canSelect (self):
        return self.selectable
