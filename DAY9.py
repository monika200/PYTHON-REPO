1.Write a function to compute divide by zero and use try/except to catch the exceptions.

try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    z=x/y
    print("Result:",z)
except Exception as arg:
    print("Exception raised:",arg)
else:
    print("Normal end of the file")
finally:
    print("Finally executed")
    
2.Write python program to check  that given number is valid mobile number or not?

import re
a=input("Enter mobile number:")
b=re.fullmatch("[7-9]\d{9}",a)
if b!=None:
    print("Valid mobile number")

else:
    print("Invalid mobile number")
    
3.Write python program to check  that given email address is valid   or not?

import re
a=input("Enter your email address:")
b=re.fullmatch("\w[_.]*@gmail[.]com",a)
if a!=None:
    print("Valid email address")
else:
    print("Invalid email address")
    
4.Write a python program to check given car registration number is valid Maharashtra state registration number or not?

import re
a=input("Enter your email address:")
b=re.fullmatch("MP[0-9]{2}[A-Z]{2}\d{4}",a)
if a!=None:
    print("Valid vehicle number")
else:
    print("Invalid vehicle number")
    
5.Write a python program to decorate arithmetic operations.

def arithmetic_operation(func):
    def operators(a,b):
        (a,b)
        print("The product is:",a*b)
        print("The division is:",a/b)
        print("The remainder is:",a%b)
    return operators
print("This is a decorator")
@arithmetic_operation
def add_subtract(a,b):
    print("The addition is:",a+b)
    print("The sutraction is:",a-b)
add_subtract(50,60)

6.Write a python program to generate Fibonacci Numbers upto 100 using generator. 

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for i in fibonacci():
    if i>100:
        break;
    print(i)
