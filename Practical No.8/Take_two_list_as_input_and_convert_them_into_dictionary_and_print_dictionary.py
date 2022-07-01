#Take two list as input and convert them into dictionary and print dictionary
print("Enter Elements of list 1:")
list1=list(map(str,input().split()))
print("Enter Elements of list 2:")
list2=list(map(str,input().split()))

#dictionary=dict(zip(list1,list2))
dictionary={}
for key in list1:
    for value in list2:
        dictionary[key]=value
        list2.remove(value)
        break
print("Dictionary is:",dictionary)
