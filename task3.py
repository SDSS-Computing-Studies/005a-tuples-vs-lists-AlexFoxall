#! python3
"""
Sort the given list by numerical value
Find the smallest and the largest value and display them:

inputs:
none

outputs:
string containing the 2 numbers:

example:
The smallest number is 3 and the largest number is 9
"""

myList = [ 3,6,5,4,6,7,8,6,5,9,4,5 ]
myList = sorted(myList)
t1 = (myList[0])
t2 = (myList[11])
t1 = str(t1)
t2 = str(t2)
print("The smallest number is " + t1 + " and the largest number is " + t2)