from CarClass import CarClass



class ParkingStall:
    
    def __init__(self, x, y, delta_x, delta_y, car = None):
        self.car = car
        self.x = x
        self.y = y
        self.delta_y = delta_y
        self.delta_x = delta_x
        #extra
        
    def DrawCell(self):
        if self.car:
            stroke(255, 255, 255)
            fill(255, 0, 0)
            print("stall got: " ,self.x, self.y, self.delta_x, self.delta_y)
            rect(self.x, self.y, self.delta_x, self.delta_y)
        else:
            stroke(255, 255, 255)
            fill(0, 255, 0)
            print("stall got: " ,self.x, self.y, self.delta_x, self.delta_y)
            rect(self.x, self.y, self.delta_x, self.delta_y)
        
    def SetCar(self, car):
        self.car = car
        
    def RemoveCar(self):
        self.car == None
        
    def IsFull(self):
        if self.car:
            return True
        return False
