from datetime import datetime
import datetime import timedelta
class cdatetime():
    def __init__(self):
        self.starttime = datetime.now()
        self.currenttime = self.starttime
    
    @staticmethod
    def Gettime():
        # Returns a Datetime Object
        return datetime.now()
    
    def findsecondsdelta(self,DatetimeObj):
        return(self.currenttime - DatetimeObj.second)
    
    def Clockticking(self):
        self.currenttime = self.currenttime + timedelta(minutes=5)
        return self.currenttime.time()
    
    def getStartTime(self):
        return self.starttime
    
    
    # timeObj = cdatetime()
    # time.sleep(5)
    # atime = cdatetime.Gettime()
    # time.sleep(10)
    # print(cdatetime.findsecondsdelta(atime))