class Time:
    def __init__(self,Hour,Min,Sec) -> None:
        self.set_Time(Hour,Min,Sec)

    def set_Time(self,Hour,Min,Sec):
        if 0<=Hour<24 and 0<=Min<60 and 0<=Sec<60:
            self.__Hour=Hour
            self.__Min=Min
            self.__Sec=Sec
        else:
            print("Incorrect Time!")
            self.__Hour=0
            self.__Min=0
            self.__Sec=0
            # raise ValueError("Incorrect Time!")

    def get_Hour(self):
        return self.__Hour
    def get_Min(self):
        return self.__Min
    def get_Sec(self):
        return self.__Sec
    
    def __repr__(self) -> str:
        return f"{self.__Hour}:{self.__Min}:{self.__Sec}"


t1=Time(2,5,56)
# t1._Time__Hour = 70
print(t1)
# print(t1._Time__Hour)
# t1.__Hour = '130'
# print(t1.__Hour())
# t2=Time(23,34,00)
# print(t2)

# print(t2.__Hour)

