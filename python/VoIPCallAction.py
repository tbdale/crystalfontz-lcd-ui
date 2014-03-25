import os
from random import randint
from Action import Action

class VoIPCallAction (Action):    
    menu   = None
    name   = ""
    number = ""
    def __init__ (self,menu,name,number):
        self.menu = menu
        self.selectable = 1
        self.name = name
        self.number = number
        self.label = ">Call " + name


    def do (self):
        print "VoIPCallAction.do():Exec "
        callFilename = "callfile."+str(randint(0,99999999))
        callFile = open("/tmp/"+callFilename,"w")
        callFile.write("""
Channel: Local/6930@default
MaxRetries: 2
RetryTime: 10
WaitTime: 30
Context: default
Extension: 1501
Priority: 1
""")
        callFile.flush()
        callFile.close()
        print "VoIPCallAction.do(): mv "+callFilename
        os.system("mv /tmp/%s /var/spool/asterisk/outgoing/" % callFilename)



