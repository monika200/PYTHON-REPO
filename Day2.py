
Que:1.
n=int(input("Enter a no:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(i,end=" ")
    if i<n:
        print("+",end=" ")
print("=",sum)



Que:2.
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



Que:3.
n=int(input("Enter a no:"))
for i in range(1,11):
    print(n*i)
    
Que.4.

def SumOddNumbers(n):
  return n*n*n
print(SumOddNumbers(4))
    
Que:5.
n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
