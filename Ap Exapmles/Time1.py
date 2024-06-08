class Time:
    def __init__(self,Hour,Min,Sec):
        self.Hour=Hour
        self.Min=Min
        self.Sec=Sec

    def __repr__(self):
        return f"{self.Hour}:{self.Min}:{self.Sec}"


t1=Time(14,23,45)
print(t1)
t2=Time(120,13,15)
print(t2)