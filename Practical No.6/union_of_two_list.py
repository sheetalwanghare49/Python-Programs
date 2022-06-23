#Program to find union of two list
n=int(input("Enter number of elements of list1:"))
list1=[]
print("Enter the elements of list1:")
for i in range (0,n):
    ele1=input()
    list1.append(ele1)

m=int(input("Enter number of elements of list2:"))
list2=[]
print("Enter the elements of list2:")
for i in range (0,m):
    ele2=input()
    list2.append(ele2)

print("List1:",list1)
print("List2:",list2)

ans=[]
for i in list1:
    if i not in ans:
        ans.append(i)
for i in list2:
    if i not in list1:
        ans.append(i)
print("The union of 2 list is:",ans)
