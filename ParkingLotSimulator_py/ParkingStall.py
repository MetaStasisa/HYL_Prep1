from CarClass import CarClass



class ParkingStall:
    
    def __init__(self, car = None):
        self.car = car
    
    def SetCar(self, car):
        self.car = car
        
    def RemoveCar(self):
        self.car == None
        
    def IsFull(self):
        if self.car:
            return True
        return False
