class leap_yr:
    def __init__(self, year):
        self.year = year
        if (self.year % 4 == 0):
            print("Not a leap year because not divisible by 4")
        elif (self.year % 100 == 0):
            print("Not a leap year because not divisible by 100")
        elif (self.year % 400 == 0):
            print("Not a leap year because not divisible by 400")
        else:
            print("Leap year")


year = input("Enter the year: ")
leap = leap_yr(year)   