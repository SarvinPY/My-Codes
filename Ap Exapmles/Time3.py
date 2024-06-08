
class Time:
    def __init__(self,Hour,Min,Sec):
        self.__Hour=Hour
        self.__Min=Min
        self.__Sec=Sec

    def __repr__(self) -> str:
        return f"{self.__Hour}:{self.__Min}:{self.__Sec}"


t1=Time(140,23,45)
print(t1)
print(t1.__Hour)

t1.__Hour=130
print(t1.__Hour)
print(dir(t1))