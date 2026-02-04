#Cleanest way to get index1
#For a list ["foo", "bar", "baz"] add an item in the list "bar", what's the cleanest way to get its index (1) in Python?
#Best way to check if a list is empty
#Getting the last element of a list in Python
#How to clone or copy a list?
#How can I count the occurrences of a list item in Python?
#How do I remove the first Item from a Python list?
#Write a program to create a buffer of length 5


list1 = ["foo", "bar", "baz" ]
list1.append('bar')
print(list1)
print(list1[1])

#Check if a list is empty
#print(list1[][])

#Getting the last element of a list in Python
x = list1.pop()
print(f"The last element in list1 is: {x}")
print(f"After the last element is popped, the current list is: {list1}")

#How to clone or copy a list?
list2 = list1.copy()
print(f"the copied list is: {list2}")

list1.append("bar")
print(list1)

#How can I count the occurrences of a list item in Python?
print(list1.count("bar"))

#How do I remove the first Item from a Python list?
print(list1.remove("bar"))
print(list1)

#Write a program to create a buffer of length 5


list1.extend("python")
print(list1)






