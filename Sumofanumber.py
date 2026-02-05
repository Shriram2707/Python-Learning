#Assignment 1: Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
number1 = input("Enter a two digit number 1 of choice:")
#number2 = input("Enter a two digit number 2 of choice:")
num1 = int(number1)
#num2 = int(number2)
sum = 0
for x in number1:
    sum = sum + int(x)
#x = num1
print(f"Sum : {sum}")