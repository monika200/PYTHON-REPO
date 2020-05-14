#1. Given a number count the total number of digits in a number
n = int(input("Enter a number:"))
count = 0
while n!= 0:
    n//= 10
    count+= 1
print("Total number of digits: ", count)

#2Reverse the following list using for loop
list1 = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input()) 
    list1.append(ele)
print("Original list:",list1)
for i in range(len(list1) - 1, -1, -1) :
    print(list1[i])
    
#3.Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
def appendMiddle(s1,s2):
    middleIndex = int(len(s1)/2)
    print("Original Strings:",s1, s2)
    middleThree = s1[:middleIndex-1:]+ s2 +s1[middleIndex-1:]
    print("After appending s2:",middleThree)
appendMiddle("Chrisdem","IamNewString")

#4.Arrange String characters such that lowercase letters should come first
inputStr = input("Enter a string:")
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = "".join(lower + upper)
print("arranging characters giving precedence to lowercase letters:",sortedString)

#5. Given a string, return the sum and average of the digits that
appear in the string, ignoring all other characters

import re
inputStr = "English = 78 Science = 83 Math = 68 History = 65"
markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
totalMarks = 0
for mark in markList:
  totalMarks+=mark
percentage = totalMarks/len(markList)  
print("Total Marks is:", totalMarks, "Percentage is ", percentage)

#6: Given a two list. Create a third list by picking an odd-index element from the first list and even index 
#elements from second.
listOne = []
n = int(input("Enter number of elements in listOne:"))
for i in range(0, n): 
    ele = int(input()) 
    listOne.append(ele)
print(listOne)
listTwo = []
x = int(input("Enter number of elements in listTwo:"))  
for i in range(0, x): 
    ele = int(input()) 
    listTwo.append(ele)
print(listTwo)
listThree = list()

oddElements = listOne[1::2]
print("Odd-index element from list one",oddElements)


EvenElements = listTwo[0::2]
print("Even-index element from list two",EvenElements)

print("Third list")
listThree.extend(oddElements)
listThree.extend(EvenElements)
print(listThree)
