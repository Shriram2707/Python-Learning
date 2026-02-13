#Sets and Tuples: Assignments
#Assignment 1:
#Difference between Sets and Frozen Sets
#1. Sets:
#Sets can have immutable data but its a mutable data type
#2. Frozen Sets:
#Frozen sets are immutable objects that only support methods and operators
# that produce a result without affecting the frozen set or sets to which they are applied.
from nt import remove

#Assignment 2:
#Remove duplicate values of a list a=[1,2,3,4,1,2,3,10]

a = [1,2,3,4,1,2,3,10]
a1 = set(a)
b = list(a1)
print(b)

#Assignment 3:
s1 = set([7,9, 12, 7, 9])
s2 = set(['abc', 12, 'b', 'car', 7, 10, 12 ])
s3 = set([12, 14, 12, 'ab'])
print (s1 & s2)
print (s1 | s2)
print ('b' in s2)
print ('ab' in s2)
print ('ab' in s3)
s2.discard(12)
print ((s1 & s2) ^ s3)

#Assignment 3:Given three sets, s1, s2, and s3, write a short segment of Python code to find the values that are in exactly one of the three sets.
# The result should be stored in a set called s.
# You may NOT use any loops.

s1 = set( [7,9, 12, 7, 9] )
s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ])
s3 = set( [12, 14, 12, 'ab'] )
print ((s1 & s2))
print((s1 & s2) ^ s3)
print((s1^s2)^(s3))
s = (s1-s2 | s2-s1)
print (s)
print(s-s3|s3-s)