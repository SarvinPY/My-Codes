# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
# man = Celsius()
# man.temperature = 37
# print(man.temperature)
# print(man.to_fahrenheit())
# class Celsius:
#     def __init__(self, temperature = 0):
#         self.set_temperature(temperature)

#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32

#     # new update
#     def get_temperature(self):
#         return self._temperature

#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         self._temperature = value
# c = Celsius(37)
# print(c.get_temperature())
# a = float(input())
# a = "{:.3f}".format(a)
# print(a)
# a = float(input())
# a = "%.4f" % a
# print(a)




class Dog:
    quantity = 0
    def __init__(self , name , age) -> None:
        self.name = name
        self.age = age
        Dog.quantity = Dog.quantity + 1
bulldog = Dog("Sammy" , 3)
hosky = Dog("Alex" , 5)
print(hosky.quantity)
















