class user():
    def __init__(self , name , family , age) -> None:
        self.name = name
        self.family = family
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self , value) :
        if value > 0 :
            self._age = value
        else :
            self._age = 0
a = user('sarvin' , 'Hosseini' , 20)
a.age = 21
print(a.age)