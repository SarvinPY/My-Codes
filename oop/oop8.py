class Student:
    def __init__(self, first, last, id, avg):
        self.first = first
        self.last = last
        self.id = id
        self.avg = avg
    def Avg_A(self):
        if self.avg>=17:
            print(self.first, self.last,self.avg,self.id)

li = []
num = int(input("Enter Number of Students : "))
for i in range(num):
    print(f"----- Student{i+1} ------")
    first = input("Enter first name = ")
    last = input("Enter last name = ")
    id = input("Enter id number = ")
    avg = float(input("Enter average = "))
    x=Student(first, last, id, avg)
    li.append(x)

for item in li:
    item.Avg_A()