Que.1.	Write a function to find max of three numbers.

def max(x,y,z):
    if x>y and x>z:
        return x 
    elif y>z:
        return y 
    else:
        return z
a=max(12,18,20)
print(a)

----------------------------------------------------------------------------------------------


Que.2.	Write a Python program to detect the number of local variables declared in a function.

def local():
    a=10
    b=20
    c=50
    d="Monika"
    
print(local.__code__.co_nlocals)


-----------------------------------------------------------------------------------------------------------------------------------
Que.3.	Write a recursive function to calculate the sum of numbers from 0 to 10
Expected output: 55

def sum(n):
    if n==0:
        return n
    else:
        return n + sum(n-1)
a= sum(10)
print(a)


-----------------------------------------------------------------------------------------------------------------------------------


4.	Create a function showStudent() in such a way that it should accept student id, name, and it’s college name  and if the id 
and college name is missing in function call it should show it as by default id is 1 and college name  is VITA.

def showStudent(std_name,std_id=1,college_name="VITA"):
        return std_id,std_name,college_name
a=showStudent("Monika",3,"xyz")
b=showStudent("Nitika")
print(a)
print(b)

------------------------------------------------------------------------------------------------------------------------------------

5.	Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]

def unique_List(list):
  list1 = []
  for i in list:
    if i not in list1:
      list1.append(i)
  return list1

a= unique_List([11,22,22,33,33,33,44,55,55,66])
print(a)


------------------------------------------------------------------------------------------------------------------------------------
6.	Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
1st for first digit
2nd for last digit
Example:
 Input:  5424
Output: 9

def first(x) : 
    while x >= 10:  
        x = x / 10
    return int(x) 
def last(x) : 
    return (x % 10) 
def sum(x,y):
    return x+y
  
number=int(input("Enter any no:"))
print("First no is",first(number))
print("Last no is",last(number))
print("Sum of first and last no is",sum(first(number),last(number)))
