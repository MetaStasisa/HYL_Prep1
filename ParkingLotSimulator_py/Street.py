import random

class Street:
    #have list with 0-10 and at index 5 check if parking and at index 10 then remove
    #constructor to draw streets
    def __init__(self):
        fill(50, 50, 50)
        rect(-5, 150, 1910, 75)
        rect(-5, 875, 1910, 75)
        self.Cars = []
        
    #draw moves cars by frame
    def MoveCars(self):
        for i in range (11):
            if self.Cars[i] != None:
                self.Cars[i].SetX(self.Cars[i].GetX() + 1900/11)
        for i in range (10, 0, -1):
            if i == 10 and self.Cars[10] != None and self.Cars[10] > 1900:
                self.Cars[10] = None
            self.Cars[i-1] = self.Cars[i]
            self.Cars[i] = None
            
        
    #randomly create cars & randomize their colour
    def CreateCars(self):
        temp = random.randint(0,1)
        if temp == 1:
            tempR = random.randint(0, 255)
            tempG = random.randint(0, 255)
            tempB = random.randint(0, 255)
            tempNumber = random.randint(10000, 99999)
            car = CarClass(0, 150, tempR, tempB, tempG, tempNumber)
            self.Cars[0] = car
        
    #when a car reaches middle (index = 6) check if parking and move accordingly
    
    #when car reaches end then make it disappear and then delete object and delete from list
        
        
    def draw():
        #if there is space at the beginning of the street then see if randomly create a car
        for car in self.Cars:
            if car:
                car.DrawCar()
        if self.Cars[0] = none or self.Cars[0].GetX() > 75:
            self.CreateCars()
        
    def GetCars(self):
        return self.Cars
        
