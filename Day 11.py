class RemoteTv():
   
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
    
    def turnOn(self):
        self.switchIsOn = True
   
    def turnOff(self):
        self.switchIsOn = False
   
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
   
    def lowerLevel(self) :
        if self.brightness > 0:
           self.brightness = self.brightness - 1

    def show(self):
        print('Switch is on ?', self.switchIsOn)
        print('Brightness is:', self.brightness)

remoteSatu = RemoteTv()

remoteSatu.turnOn()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.show()

remoteSatu.lowerLevel()
remoteSatu.lowerLevel()
remoteSatu.turnOff()
remoteSatu.show()