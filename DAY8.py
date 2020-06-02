1.	Write a program to implement Constructor with Variable Number of Arguments.

class Sum:
    def __init__(self,*args):
        print("sum of numbers is",sum(args))
a=Sum(1)
b=Sum(1,2)
c=Sum(1,2,3)
d=Sum(1,2,3,4)
e=Sum(1,2,3,4,5)



3.	Write a program to implement multiple inheritance.

class Parent1:
    def Sum(self,a=10,b=20):
        print("Parent1 method",a+b)

class Parent2:
    def Sum(self,a=20,b=30):
        print("Parent2 method",a*b)
class Child(Parent1,Parent2):
    pass

c=Child()
c.Sum()

4.	Write a program to implement operator overloading in python.

class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Sum(self):
        print("The addition of:",self.a+self.b)

a=Addition(50,70)
a.Sum()
a1=Addition("Hello","World")
a1.Sum()

5.	 Write a Python program to square and cube every number in a given list of integers using Lambda. 


List = [2, 3, 4, 5, 6, 7, 8]
sq = list(map(lambda x: x ** 2, List))
print(sq)
cube = list(map(lambda x: x ** 3, List))
print(cube)
