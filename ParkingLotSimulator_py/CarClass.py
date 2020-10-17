class CarClass:
    def __init__(self, car_colour, car_number):
        self.car_colour = car_colour
        self.car_number = car_number
    
    def GetAttributes(self):
        dict_car = {
        "car_colour": self.car_colour,
        "car_number": self.car_number
        }
        return dict_car
