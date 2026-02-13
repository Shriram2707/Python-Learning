#The marks obtained by a student in 5 different subjects are input  // through the keyboard.
# The student gets a // # division as per the following rules:
# Percentage above or equal to 60 - // First division //
# Percentage between 50 and 59 - Second division //
# Percentage between 40 and 49 - Third division //
# Percentage less than 40 - Fail //
# Write a program to calculate the division obtained by the student
from ctypes.wintypes import MAX_PATH

Physics = int(input("Enter your Physics marks: "))
Chemistry = int(input("Enter your Chemistry marks: "))
Math = int(input("Enter your Math marks: "))
Science = int(input("Enter your Science marks: "))
Language = int(input("Enter your Language marks: "))

if Physics >= 60:
            print(Physics, " Physics:First Division")
elif Physics > 50 and Physics <= 59:
        print(Physics, "Physics: Second Division")
elif Physics > 40 and Physics <= 49:
            print(Physics, "Physics: Third Division")
else:
        print(Physics, "Physics: Fail")

if Chemistry >= 60:
    print(Chemistry, "Chemistry: First Division")
elif Chemistry > 50 and Chemistry <= 59:
    print(Chemistry, "Chemistry:Second Division")
elif Chemistry > 40 and Chemistry <= 49:
    print(Chemistry, "Chemistry:Third Division")
else:
    print(Chemistry, "Fail")

if Math >= 60:
    print(Math, "Math:First Division")
elif Math > 50 and Math <= 59:
    print(Math, "Math:Second Division")
elif Math > 40 and Math <= 49:
    print(Math, "Math:Third Division")
else:
    print(Math, "Math:Fail")

if Science >= 60:
    print(Science, "Science:First Division")
elif Science > 50 and Science <= 59:
    print(Science, "Science:Second Division")
elif Science > 40 and Science <= 49:
    print(Science, "Science:Third Division")
else:
    print(Science, "Science:Fail")

if Language >= 60:
    print(Language, "Language: First Division")
elif Language > 50 and Language <= 59:
    print(Language, "Language: Second Division")
elif Language > 40 and Language <= 49:
    print(Language, "Language: Third Division")
else:
    print(Language, "Language: Fail")
