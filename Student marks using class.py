class division:
    def __init__(self, agg_marks):
        self.agg_marks = int(agg_marks)
        if (self.agg_marks >= 60):
            print("First Division")
        elif ((self.agg_marks >= 50) and (self.agg_marks < 59)):
            print("Second Division")
        elif ((self.agg_marks >= 40) and (self.agg_marks < 49)):
            print("Third Division")
        else:
            print("Fail")


sub1 = int(input("Maths = "))
sub2 = int(input("Computer = "))
sub3 = int(input("Chemistry = "))
sub4 = int(input("Physics = "))
sub5 = int(input("English = "))
aggregate_marks = (sub1 + sub2 + sub3 + sub4 + sub5) / 500 * 100
#agg_marks = int(aggregate_marks)
print(f"The aggregate marks is : {agg_marks}")
student = division(agg_marks)