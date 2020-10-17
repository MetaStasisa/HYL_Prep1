class CarClass:
    def __init__(self, car_colour, car_number):
        self.car_colour = car_colour
        self.car_number = car_number
    
    def GetAttributes(self):
        return dict_car{"car_colour": f"{self.car_colour}",
                          "car_numer": self.car_number}
    
    
    
