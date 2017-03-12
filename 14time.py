class time:
    hour=0
    minute=0
    second=0
    def __init__(self):
        self.hour=0
        self.minute=0
        self.second=0
    def get(self):
        print('Hours = '+str(self.hour),'Minutes = '+str(self.minute),'Seconds = '+str(self.second))
    def setTime(self,elapse_Time):
        et=elapse_Time
        self.hour=et//3600
        et=et%3600
        self.minute=et//60
        et=et%60
        self.second=et
Time=time()
Time.setTime(555550)
Time.get()
