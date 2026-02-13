#Any integer is input through the keyboard.
# Write a program to find out
# whether it is an odd number or even number.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    if num % 2 != 0:
        print("Odd")
