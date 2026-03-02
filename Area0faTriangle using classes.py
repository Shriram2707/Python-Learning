class area:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area_cal(self):
        return (self.a*self.b)


a = int(input("enter width: "))
b = int(input("enter length: "))

c = area(a,b)

print(f"The area of the rectangle is: {c.area()}")