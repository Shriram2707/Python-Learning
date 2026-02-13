#The current year and the year in which the employee joined the
#// organization are entered through the keyboard.
# If the number of years for which the employee has // # served the organization is greater than 3 then a bonus of Rs. 2500/- is // given to the employee.
# If the years of service are not greater // # than 3, then the program should do nothing. //

Current_year = int(input("Enter the Current Year: "))
Emp_year_join = int(input("Enter the Employee Year: "))
if (Current_year - Emp_year_join) > 3:
    print("Congrats! Employee is eligible for a bonus of $2500.")
else:
    print("Byeee.....")
    