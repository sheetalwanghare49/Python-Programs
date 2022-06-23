#Program to remove the ith occurrence of given word in a list where words repeat
a=[]
n=int(input("Enter the number of elements in list:"))
ele=input("Enter element in list:")
for x in range(0,n):
    ele=input()
    a.append(ele)
print(a)
c=[]
count=0
b=input("Enter a word to remove: ")
o=int(input("Enter the occurrence to remove: "))
for i in a:
    if(i==b):
        count=count+1
        if(count!=o):
            c.append(i)
    else:
         c.append(i)
if(count==0):
    print("Item not found")
else:
    print("The number of repetition is:",count)
    print("The updated list is:",c)

      
