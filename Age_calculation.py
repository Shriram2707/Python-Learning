#Assignment 3: Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("Please enter your Age" "** Average life-expectancy is 90 years**:: ")
age1 = int(age)
age_left = 90 - age1
print(f"You have {age_left} years more left to live.")
Days = age_left * 365
Weeks = age_left * 52
Months = age_left * 12
print(f"You have {Days} days, {Weeks} weeks, and {Months} months left.")

