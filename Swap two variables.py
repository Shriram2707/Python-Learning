#Using 3rd variable
a = 10
b = 20
c = a
a = b
b = c
print (a)
print (b)

#Without using 3rd variable
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a)
print(b)

### USING USER-INPUT:
#Swap using 3rd variable

print("Enter the 1st number: ")
num1 = int(input())
print("Enter the 2nd number: ")
num2 = int(input())
num3 = num1
num1 = num2
num2 = num3
print(f"Swapped numbers are: {num1, num2}")

#Without the 3rd variable

print("Enter the 1st number: ")
num3 = int(input())
print("Enter the 2nd number: ")
num4 = int(input())
num3 = num3 + num4
num4 = num3 - num4
num3 = num3 - num4
print(f"Swapped numbers are: {num3, num4}")

