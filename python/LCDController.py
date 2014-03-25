import serial,crc16,struct
import time

class LCDController:
    """
    Controller class for the CrystalFontz 635 LCD Display
    Author: Brian Dale
    Date: May 10, 2007
    """

    conn = None

    CURSOR_STYLE_NONE   = 0
    CURSOR_STYLE_BLINK  = 1
    CURSOR_STYLE_UNDER  = 2
    CURSOR_STYLE_BLINKBLOCKUNDER = 3
    CURSOR_STYLE_INVERT = 4

    def __init__ (self, comPort=0):
        """ 
           Class Constructor 
           - Initialize serial communications
        """
        self.conn = serial.Serial(comPort,             \
                                  115200,              \
                                  serial.EIGHTBITS,    \
                                  serial.PARITY_NONE,  \
                                  serial.STOPBITS_ONE, \
                                  0,                   \
                                  0,                   \
                                  0,                   \
                                  None,                \
                                  None)
        self.initComm()
        return

    def clearScreen (self):

        reply = None
        crc = crc16.CRC16()
        cmd = "\x06"
        data = ""
        self.sendPacket(cmd,data)

        return 

    def getFirmware (self):

        reply = None
        crc = crc16.CRC16()
        cmd = "\x01"
        data = ""
        self.sendPacket(cmd,data)
        reply = self.receive()
        
        return reply[1]

    def reboot (self):
        reply = None
        crc = crc16.CRC16()
        cmd = "\x05"
        data = "\x08\x12\x63"
        self.sendPacket(cmd,data)
        reply = self.receive()
                
        return reply[1]

    def sendText( self, row=0, col=0, text ="" ):

        reply = None
        cmd = "\x1F"
        data = chr(col) + chr(row)
        data += text[:20]
        reply = self.sendPacket(cmd,data)

        return reply

    def setCursor (self,row=0,col=0,style=0):

        reply = None
        cmd   = "\x0c"
        data  = style
        reply = self.sendPacket(cmd,data)

        cmd   = "\x0b"
        data  = chr(col) + chr(row)
        reply = self.sendPacket(cmd,data)

        cmd   = "\x0c"
        data  = 0
        reply = self.sendPacket(cmd,data)

        return reply

    def setLed (self, row, green, red):

        reply = None
        cmd = "\x22"
        led = 0
        if red < 101 and green < 101:
            if row == 0 : led = [11,12]
            if row == 1 : led = [ 9,10]
            if row == 2 : led = [ 7, 8]
            if row == 3 : led = [ 5, 6]
    
            data = chr( led[0] ) + chr(green)
            self.sendPacket(cmd,data)
            data = chr( led[1] ) + chr(red)
            self.sendPacket(cmd,data)

        return 

    def scanKeys(self):
        self.initComm()
        self.sendPacket( chr(24) ,"")
        reply = self.receive()
        if reply == None : return None # Receive error
        if ord(reply[0]) != (0x40 | 24) : return None # Wrong packet return type

        data = reply[1]
        keyStats = {"currently_pressed"   : data[0] , \
                    "pressed_since_last"  : data[1],  \
                    "released_since_last" : data[2] }

        
        return keyStats

    def receive (self):
        #time.sleep(0.01)
        retryCount = 0
        msgType = ""
        while retryCount < 15 and msgType == "":
            msgType = self.conn.read(1)
            if msgType == "" : time.sleep(0.02)
            retryCount += 1
        
        if msgType == None or msgType == "" : 
            self.initComm()
            return None # Unable to receive message type part

        msgLen = self.conn.read(1)
        if msgLen == None  or msgLen == ""  : 
            self.initComm()
            return None # Unable to receive message length part

        msg = self.conn.read( ord(msgLen) )

        mCRC = self.conn.read(2)
        if mCRC == None or len(mCRC) < 2    : 
            self.initComm()
            return None # Unable to receive CRC part

        dataCRC = ord(mCRC[0]) + (ord(mCRC[1]) << 8)
        crc = crc16.CRC16() 
        crc.update(msgType + msgLen + msg)
        if crc.getValue() != dataCRC: 
            self.initComm()
            return None # CRC error
        
        return [msgType,msg]


    def sendPacket (self, cmd, data):
        crc = crc16.CRC16()
        cmd += chr( len (data) ) + data
        crc.update(cmd)
        csum = crc.getValue()
        packet  = cmd + chr(csum & 0x00FF) + chr(csum >> 8);
        
        self.conn.write(packet)
        self.conn.flush()

        time.sleep(0.005) #seems to need a little delay to flush
     
        return 

    def initComm (self):
        self.sendPacket("\x01","") # clear any in buffer
        time.sleep(0.02)
        self.conn.read(8000)       # clear any in buffer
                                   # 
        return

