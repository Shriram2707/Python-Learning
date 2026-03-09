class area:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area_cal(self):
        return (self.a*self.b)


width = int(input("enter width: "))
length = int(input("enter length: "))

my_shape = area(width,length)
result = my_shape.a * my_shape.b
print(f"The area of the rectangle is: {result}")