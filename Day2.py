
Que:1.Python Program to Read a Number n And Print the Series “1+2+…..+n= “
sample:Enter a number: 4
1 + 2 + 3 + 4 = 10 

n=int(input("Enter a no:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(i,end=" ")
    if i<n:
        print("+",end=" ")
print("=",sum)

-------------------------------------------------------------------------------------------------

Que:2.Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("No of even no is:",even_count)
print("No of odd no is:",odd_count)

--------------------------------------------------------------------------------------------------

Que:3.Write a Python program to create the multiplication table (from 1 to 10) of a number. 


n=int(input("Enter a no:"))
for i in range(1,11):
    print(n*i)
 

--------------------------------------------------------------------------------------------------

Que.4.Given the triangle of consecutive odd  numbers 
Example we call function :- row_sum_odd_numbers(2)
Result will be=3 + 5 = 8
if user give 4 then ur output is 13 + 15 + 17+ 19 = 64


def rowSumOddNumbers(n):
  return n*n*n
print(SumOddNumbers(4))
 
-------------------------------------------------------------------------------------------------   
    
    
Que:5. Write python program to print the pattern given below
Note: Take input from user
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
