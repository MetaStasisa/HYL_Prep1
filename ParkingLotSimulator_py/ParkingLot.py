from ParkingStallSection import ParkingStallSection
from CarClass import CarClass
import random


class ParkingLot:    
    def __init__(self,n_sections,n_stalls):
        # n_stalls initialized for later
        self.n_stalls = n_stalls
        if n_sections > 0:
            self.sections_dict = sections_dict={}
            for i in range(n_sections):
                sections_dict[i] = ParkingStallSection(n_stalls)
        
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
                list_of_not_full = [tuplepair[0] for tuplepair in self.sections_dict.items() if not tuplepair[1].isFull()]
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
                list_of_not_empty = [tuplepair[0] for tuplepair in self.sections_dict.items() if not tuplepair[1].isEmpty()]
                rand_sec = random.choice(list_of_not_empty)
                self.sections_dict[rand_sec].PopCar()
                return True
            else:
                return False
        else:
            return False