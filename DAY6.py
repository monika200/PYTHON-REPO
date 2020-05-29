1.	Python program to Swap Keys and Values in Dictionary.

d1 = {"k1" : 1,"k2" : 2,"k3" : 3,"k4" : 4,"k5" : 5}
d2= dict([(j, i) for i, j in d1.items()]) 
print(d2)

2.	Write program to implement Selection sort.

list=[60, 50, 40, 70, 80]
print(list)
for i in range(len(list)):
    a=min(list[i:])
    index=list.index(a)
    list[i],list[index]=list[index],list[i]
print(list)

3.	Write program to implement Insertion sort.

list=[50,60,80,90,40]
for i in range(1,len(list)):
    current=list[i]
    index=i
    while current<list[index-1] and index>0:
        list[index] = list[index-1]
        index=index-1
        list[index]=current
print(list)

4.	Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list.
Given list: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
Sub List to be added = ["h", "i", "j"]
Expected output:-
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)

5.	Access the value of key “history”
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
Expected output: 80

sampleDict = { "class":{ "student":{ "name":"Mike", "marks":{ "physics":70,"history":}}}}
sampleDict["class"]["student"]["marks"]["history"]



