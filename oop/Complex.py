class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imag=i
    def show(self):
        if self.imag>0:
            print(f"{self.real}+{self.imag}i")
        elif self.imag<0:
            print(f"{self.real}{self.imag}i")
        else:
            print(f"{self.real}")
    def __add__(self,other):
        self.real=self.real+other.real
        self.imag=self.imag+other.imag
    def __sub__(self,other):
        self.real=self.real-other.real
        self.imag=self.imag-other.imag
    def __mul__(self,other):
        r1=(self.real*other.real-self.imag*other.imag)
        i1=(self.real*other.imag+other.real*self.imag)
        return Complex(r1,i1).show()
    def __eq__(self,other ) :
        if self.real== other.real and self.imag==other.imag :
            return True
        else:
            return False



x=Complex(30,5)
y=Complex(3,5)
z=x*y
# z.show()
# print(x==y)



# z=x.mul(y)

# if x==y:
#     print("barabar")
# else:
#     print("Nabarabar")



# x.add2(y)
# x.show()


# r=float(input("Enter a Number for real part: "))
# i=float(input("Enter a Number for imaginary part: "))
