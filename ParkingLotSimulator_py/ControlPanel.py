class ControlPanel:
    
    def __init__(self, time_elapsed, customers):
        self.time_elapsed = time_elapsed
        self.customers = customers
        
        
        
    def drawUI(self):
        
        stroke(255, 255, 255)
        fill(0, 100, 0)
        rect(0, 0, 1900, 100)
        
        #Draw Parking Rates:
        stroke(0, 0, 0)
        fill(50)
        rect(20, 10, 300, 80)
        #Draw Text:
        textSize(15)
        fill(0)
        text("Parking Rates:", 30, 30)
        textSize(10)
        text("$3.00 / Hour   Mon-Fri              8AM to 6PM", 30, 45)
        text("$2.00 / Hour   Saturday             8AM to 6PM", 30, 60)
        text("$1.50 / Hour   All Other Times", 30, 75)
        
        #Draw Stop Play Section:
        fill(50)
        rect(850, 10, 200, 80)
        #Draw Play Circle:
        circle(900, 50, 70)
        #Draw Play Button:
        triangle(890, 30, 890, 70, 920, 50)
        #Draw Pause Circle:
        circle(1000, 50, 70)
        
        
        #Draw Simulation Values:
        rect(1400, 15, 230, 70)
        #Draw Text
        textSize(15)
        fill(0)
        x= 10
        text("Simulation Values", 1410, 30)
        textSize(10)
        text("Net Profits:        $" + str(x), 1410, 45)
        text("Time Elapsed:    $" + str(x), 1410, 60)
        text("Customers :       $" + str(x), 1410, 75)
