Que.1.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

list = [1,4,3,8,5,6,12,8,2,10]
square_list=[]
for i in list:
    square_list.append(i*i)
print(square_list)


--------------------------------------------------------------------------------------------------------------------------


Que.2.From a list containing ints, strings and floats, make three lists to store them separately

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

-------------------------------------------------------------------------------------------------------------------------

Que.3.Print the pattern
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5


n=int(input("Enter a no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

---------------------------------------------------------------------------------------------------------------------------    
    
    
Que.4.Accept data in two 3*3  matrix and calculate the sum of the matrices.

x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[10,11,12],[13,14,15],[16,17,18]]
z=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j] + y[i][j]

for k in z:
    print(k)

    
-------------------------------------------------------------------------------------------------------------------------    
    
Que.5.Write a Python program to check whether a given number is a narcissistic number or not
For example, 371 is a narcissistic number; it has three digits, and if we cube each digits  33 + 73 + 13 the sum is 371. 

n=int(input("Enter a no:"))
sum = 0
for x in str(n):
    sum += (int(x) ** len(str(n)))
if sum == n:
    print(n,"is a narcissistic number")
else:
    print(n,"is not a narcissistic number")
