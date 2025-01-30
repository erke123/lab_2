class Time:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s
    
    def __str__(self):
        rh = "0"
        rm = "0"
        rs = "0"
        if self.hours//10<1:
            rh+=str(self.hours)
        else:
            rh=str(self.hours)
        if self.minutes//10<1:
            rm+=str(self.minutes)
        else:
            rm=str(self.minutes)
        if self.seconds//10<1:
            rm+=str(self.seconds)
        else:
            rm=str(self.seconds)

        return rh+':'+rm+':'+ rs
        
    def increment_min(self):
        if self.minutes==59:
            if self.hours==23:
                self.hours=0
                self.minutes=0
            
            else:
                self.hours+=1
                self.minutes=0
            
        else:
            self.minutes+=1
            self.hours=+1
    def increment_sec(self):
        if self.seconds==59:
            if self.minutes==59:
                if self.hours==23:
                    self.seconds=0
                    self.minutes=0
                    self.hours=0
                else:
                    self.hours=+1
                    self.minutes=0
                    self.seconds=0
            else:
                self.minutes=+1
                self.seconds=0
        else:
            self.seconds=+1
            self.minutes=+1
            self.hours=+1
    def decrement_min(self):
        if self.minutes == 0:
            if self.hours == 0:
                self.hours = 23
                self.minutes=59
            else:
                self.hours =-1
                self.minutes=59
            
        else:
            self.minutes=-1
    def decrement_sec(self):
        if self.seconds == 0:
            if self.minutes==0:
                if self.hours ==0:
                    self.hours = 23
                    self.minutes=59
                    self.seconds=59
                else:
                    self.hours =-1
                    self.minutes=59
                    self.seconds=59
            else:
                self.minutes =-1
                self.seconds=59
        else:
            self.seconds =-1


        








            
time = Time(6, 59, 59)  
time.increment_sec()
print(time.__str__())
