import random

class CarClass:
    def __init__(self, car_x, car_y, car_R, car_G, car_B, car_number):
        
        self.car_x = car_x
        self.car_y = car_y
        self.RGB = [car_R, car_G, car_B]
        self.car_number = car_number
        self.IsParking = random.randint(0, 1)
        self.DrawCar(self)
        
    def DrawCar(self):
        noStroke()
        fill(self.RGB[0], self.RGB[1], self.RGB[2])
        rect(self.car_x, self.car_y, self.75, self.50)
        if self.IsParking == 1:
            fill(255, 255, 255)
            text("PARKING", self.car_x - 10, self.car_y - 10)
    
    def GetR(self):
        return self.RGB[0]
    
    def GetG(self):
        return self.RGB[1]
    
    def GetB(self):
        return self.RGB[2]
    
    def GetNumber(self):
        return self.car_number
    
    def GetX(self):
        return self.car_x
    
    def GetY(self):
        return self.car_y
    
    def SetR(self, car_R):
        self.RGB[0] = car_R
        
    def SetG(self, car_G):
        self.RGB[1] = car_G
        
    def SetB(self, car_B):
        self.RGB[2] = car_B
        
    def SetX(self, car_x):
        self.car_x = car_x
        
    def SetY(self, car_y):
        self.car_y = car_y
    
