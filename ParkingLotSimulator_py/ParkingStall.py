from CarClass import CarClass



class ParkingStall:
    
    def __init__(self, car = None, x, y, colour):
        self.car = car
        self.x = x
        self.y = y
        self.colour = colour
    
    def DrawCell(self):
        fill(self.colour[0]
        rect(self.x, self.y, 82.5, 65)
    def SetCar(self, car):
        self.car = car
        
    def RemoveCar(self):
        self.car == None
        
    def IsFull(self):
        if self.car:
            return True
        return False
