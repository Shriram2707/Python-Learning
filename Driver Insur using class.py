class empbonus:
    def __init__(self, curr_yr, doj):
        self.curr_yr = int(curr_yr)
        self.doj = int(doj)
        yrs_worked = self.curr_yr - self.doj
        if (yrs_worked > 3):
            print("You are eligible for a bonus of $2500")
        else:
            print("You're not eligble")


emp_doj = input("Please enter your Date of Joining: ")
emp_curryr = input("Please enter the current year: ")

employee = empbonus(emp_curryr, emp_doj)