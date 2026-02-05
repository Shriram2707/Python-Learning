#Assignment 2: #Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
weight = input("Please enter your weight:")
wt1 = float(weight)
height = input("Please enter your height:")
ht1 = float(height)
BMI = wt1 / (ht1 * ht1)
BMI1 = int(BMI)
print(f"Your Body Mass Index is: {BMI1}")
