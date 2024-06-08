class Time:
    def __init__(self,Hour,Min,Sec):
        if 0<=Hour<24 and 0<=Min<60 and 0<=Sec<60:
            self.Hour=Hour
            self.Min=Min
            self.Sec=Sec
        else:
            # raise ValueError("Incorrect Time!")
            print("Incorrect Time!")
            self.Hour=-1
            self.Min=-1
            self.Sec=-1

    def __repr__(self) -> str:
        return f"{self.Hour}:{self.Min}:{self.Sec}"


# t1=Time(14,23,45)
# print(t1)
t2=Time(2,23,17)
print(t2)
t2.Hour=89
print(t2)