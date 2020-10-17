from ParkingStallSection import ParkingStallSection
from CarClass import CarClass
import random


class ParkingLot:    
    lotWidth = 1800
    lotHeight = 600
    streetWidth = 75

    def __init__(self,n_sections,n_stalls,x,y):
        # n_stalls initialized for later
        self.n_stalls = n_stalls
        self.x = x
        self.y = y
        if n_sections > 0:
            self.sections_dict = sections_dict={}
            for i in range(n_sections):
                sections_dict[i] = ParkingStallSection(n_stalls)
        self.draw()

    def draw(self):
        stroke(255,255,255)
        # Drawing the parking lot itself
        rect(self.x, self.y, self.lotWidth, self.lotHeight)

        # Drawing street through the middle
        x_middle = (self.lotWidth-self.streetWidth*2)/2
        rect(x_middle, (self.y-self.streetWidth*2)/2, self.streetWidth, self.lotHeight + 2*self.streetWidth)

        section_length = (self.lotWidth-self.streetWidth*2)/2
        section_height = (self.lotHeight-100)/len(self.sections_dict)
        section_x = 50+self.x
        section_y = 100+self.y
        y_mult = 1
        for i in range(len(self.sections_dict)):
            if i%2==0:
                self.sections_dict[i].draw(section_x,section_y*y_mult,section_length,section_height)
            else:
                self.sections_dict[i].draw(section_x+x_middle,section_y*y_mult,section_length,section_height)
                y_mult+=1
            
        
    def getN_Sections(self):
        """Returns the n_sections in the Parking lot

        Returns:
            int: The number of sections in Parking Lot
        """
        return len(self.sections_dict)
    
    def setN_Sections(self,n_sections):
        """
        Changes n_sections to the provided value
        
        Removes or adds stall sections based on if the number is higher or lower
        than the existing n_sections 
        
        Returns:
            int: The number of sections in Parking Lot once they've been modified
        
        """
        # n_stalls initialized for later
        n_stalls = 8
        current_n_sections = self.getN_Sections()
        if n_sections > current_n_sections:
            for i in range(current_n_sections,n_sections):
                self.sections_dict[i] = ParkingStallSection(n_stalls)
        elif n_sections < current_n_sections:
            for i in range(n_sections, current_n_sections):
                del self.sections_dict[i]
        return self.getN_Sections()
    
    def IsFull(self):
        """
        Checks if all of the Parking lot is full by checking all the stalls in it
        
        Returns:
            Boolean: True if Parking lot is full, False otherwise
        """
        for stall_section in self.sections_dict.values():
            if not stall_section.isFull():
                return False
        return True

    def IsEmpty(self):
        """
        Checks if all of the Parking lot is empty by checking all the stalls in it
        
        Returns:
            Boolean: True if Parking lot is empty, False otherwise
        """
        for stall_section in self.sections_dict.values():
            if not stall_section.Empty():
                return False
        return True

    def PushCar(self,Car):
        if self.getN_Sections()>0:
            if not self.IsFull():
                list_of_not_full = [tuplepair[0] for tuplepair in self.sections_dict.items() if not tuplepair[1].IsFull()]
                rand_sec = random.choice(list_of_not_full)
                self.sections_dict[rand_sec].PushCar(Car)
                return True
            else:
                return False
        else:
            return False



    def ClearLot(self):
        for stall_section in self.sections_dict.values():
            stall_section.EmptySpots()
        return True

    def PopCar(self):
        if self.getN_Sections()>0:
            if not self.IsEmpty():
                list_of_not_empty = [tuplepair[0] for tuplepair in self.sections_dict.items() if not tuplepair[1].IsEmpty()]
                rand_sec = random.choice(list_of_not_empty)
                self.sections_dict[rand_sec].PopCar()
                return True
            else:
                return False
        else:
            return False

if __name__=="__main__":
    testLot = ParkingLot(5,10)
    print(testLot.getN_Sections())
    print("Is Empty")
    print(testLot.IsEmpty())
    print("Adding Cars")
    testLot.PushCar(CarClass(10,1))
    print("Is Empty")
    print(testLot.IsEmpty)
