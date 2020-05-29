1.	Write python program to perform bank operations using class and objects.
       Conditions:
a.	Bank name should be static.
b.	Using menu driven program.
1 .Deposit
2. Withdraw
3. Exit


class BankAccount:
    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("funds not available")
        self.balance -= amount

    def get_balance(self): 
        return self.balance

customer = BankAccount("Monika")
customer.deposit(2000)
customer.withdraw(1000)
print(customer.get_balance())



2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius*self.radius*3.14
    def perimeter(self):
        return 2*self.radius*3.14
a = Circle(5)
print(a.area())
print(a.perimeter())



3. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Hints:
To override a method in super class, we can define a method with the same name in the super class.

class Shape:
    def __init__(self):
        pass
    def area(self):
        print(0)
    
class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length*self.length
        
a=Square(12)
print(a.area())


4. Write a program to count how many reference variables in a program. 

import sys
a=800
b=a
c=b
d=c
print(sys.getrefcount(a)



5. write any program to achieve composition in Python

def composite(a, m): 
    return lambda x : m(a(x)) 
def add(x): 
    return x + 2
def multiply(x): 
    return x * 2
add_mul = composite(multiply, add) 
print(add_mul(5)) 
