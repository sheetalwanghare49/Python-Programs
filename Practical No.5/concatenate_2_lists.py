#Python program which concatenate 2 lists
list1 = ['p','q']
print("list1:",list1)
list2 = [1,2,3,4]
print("list2:",list2)
list = [x+str(y) for x in list1 for y in list2]
print("list after concatenation:",list)
