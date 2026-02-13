#A company insures its drivers in the following cases:
#If the driver is married.
#If the driver is unmarried, male & above 30 years of age.
#If the driver is unmarried, female & above 25 years of age.
#In all other cases the driver is not insured. If the marital status, sex
#and age of the driver are the inputs, write a program to determine
#whether the driver is to be insured or not.


mar_stats = input("Enter your Marital Status: T/F: ").upper()
sex = input("Enter your ses: M/F: ").upper()
age = int(input("Enter your age: "))

if mar_stats == "True":
    print("You are Insured")
elif mar_stats == "False" and sex == "F" and age >= 25:
    print("You are Insured")
elif mar_stats == "False" and sex == "M" and age >= 30:
    print("You are Insured")
else:
    print("You are Not Insured")