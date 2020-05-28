1.	Write a Python program to sort a list of elements using the bubble sort                                
Algorithm.

list  = [10,20,30,50,70]
print("unsorted",list)
for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            list[j] ,list[j+1] = list[j+1],list[j]
print("sorted",list)



2.	Write a Python program for sequential search (Linear search).

list=[10,20,30,50,70]
key=int(input("Enter key "))
for i in range(len(list)):
    if key==list[i]:
        print("key found")
        break
else: 
    print("key not found")
    
    
    
3.	Write a Python program for Binary search.

list=[10,30,40,10,60,70]
list.sort()
print(list)
key=int(input("Enter key "))
low = 0
high = len(list)-1
Found=False
while low<=high and not Found:
    mid = (low+high)//2
    if key==list[mid]:
        Found=True
    elif key>list[mid]:
        low=mid+1
    else:
        high=mid-1
if Found == True:
    print("key found")
else:
    print("key not Found")
    
    
    
4.	Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]

List1 = ["M","na","i","lak"]
List2 = ["y","me","s","han"]
list3 = [i+j for i,j in zip(List1,List2)]
print(list3)



5.	Iterate a given list and check if a given element already exists in a       dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}

list = [47, 64, 69, 37, 76, 83, 95, 97]
dict = {"John":47,"Peter":64,"Mahi":37,"Maria":76}
list = [i for i in list if i in dict.values()]
print(list)

