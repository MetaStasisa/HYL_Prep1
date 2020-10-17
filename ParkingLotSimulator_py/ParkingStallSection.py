from ParkingStall import ParkingStall
import random

class ParkingStallSection:
    def __init__(self, x, y, deltax, deltay,maximum=8):
        self.iNumberofcars = 0
        self.iMaximumcars = maximum
        self.xorigin = x
        self.yorigin = y
        self.width = deltax
        self.height = deltay
        self.x = self.xorigin
        self.y= self.yorigin
        
        self.dParkingStalls = self.Initialize()
        
    def Initialize(self):
        dTemporaryContainer = dict()
        for i in range(self.iMaximumcars):
            strTemp = self.__ConstructKey(i)
            # Calling Stall Class
            if i < self.iMaximumcars/2:
                dTemporaryContainer['strTemp'] = ParkingStall(self.x,self.y, self.width, self.height)
                self.x = self.x + self.width
                
            elif i == self.iMaximumcars/2:
                self.x = self.xorigin
                self.y = self.yorigin+self.height
                dTemporaryContainer['strTemp'] = ParkingStall(self.x, self.y, self.width, self.height)
                self.x = self.x + self.width
            else:
                dTemporaryContainer['strTemp'] = ParkingStall(self.x, self.y, self.width, self.height)
                self.x = self.x + self.width
        return dTemporaryContainer
    
    def draw(self):
        for item in self.dParkingStalls.values():
            item.DrawCell()
    
    
    
    def IsEmpty(self):
        if self.iNumberofcars == 0:
            return True
        else:
            return False
        
    def IsFull(self):
        if self.iNumberofcars==self.iMaximumcars:
            return True
        else:
            return False
        
    def PopCar(self):
        while True:
            iTemp = random.randint(0, self.iMaximumcars)
            sTemp = self.__ConstructKey(iTemp)
            # If Empty then Move on to next stall
            if not self.__CheckifStallisUsed(sTemp):
                continue
            self.dParkingStalls[sTemp].removeCar()
            break
        return False
            
    def PushCar(self, aCar):
        while True:
            iTemp = random.randint(0, self.iMaximumcars)
            sTemp = self.__ConstructKey(iTemp)
            # If Full move on to next stall until you get empty
            if self.__CheckifStallisUsed(sTemp):
                continue
            self.dParkingStalls[sTemp].SetCar(aCar)
            break
        return True
    
    def __ConstructKey(self, stall):
        return "stall" + str(stall)
    
    def __CheckifStallisUsed(self, stall):
        """ Receives a string and calls constructor, Returns true or false if stall is fill """
        if (self.dParkingStalls[stall].isFull()):
            return True
        
        
        
    
        
    
