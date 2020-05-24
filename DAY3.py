Que.1.

list = [1,4,3,8,5,6,12,8,2,10]
square_list=[]
for i in list:
    square_list.append(i*i)
print(square_list)


Que.2.

list = [1,3,5,"abc","are",1.24,2.56,"the","4",3.76]
string_list=[]
interger_list=[]
floats_list=[]
for i in list:
    if type(i)==str:
        string_list.append(i)
    if type(i)==int:
        interger_list.append(i)
    if type(i)==float:
        floats_list.append(i)
print(string_list)
print(interger_list)
print(floats_list)  



Que.3.

n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
Que.4.

import numpy as np
a=np.arange(2,11).reshape(1,3,3)
b=np.arange(3,12).reshape(1,3,3)
c=np.zeros((1,3,3))
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]

for k in c:
    print(k)

Que.5.

n=int(input("Enter a no:"))
sum = 0
for digit in str(n):
    sum += (int(digit) ** len(str(n)))
    if sum == n:
        print(n,"is a narcissistic number")
        break
else:
    print(n,"is not a narcissistic number")
