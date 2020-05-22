1.list=list()
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        list.append(i)
print(list)

2.n=int(input(""))
d={}    
for i in range(1,n+1):
      d[i]=i*i
print(d)

3. a=(input())
b=(input())
c=a.upper()
d=c.upper()
print(c)
print(d)


4.n=int(input("Enter a no:"))
if n%2==0:
    print("Number is even")
else:
    print("Number is odd")
    
5.age = int(input("Please enter your age:"))
if 8<=age<=12:
     print("you are allowed… welcome!!")
else:
     print("Sorry not allowed ..Bye!")
