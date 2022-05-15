#Copy all elements of one array into another
arr1=[3,8,9,5,1,4]
arr2=[None]*len(arr1)

for i in range(0,len(arr1)):
    arr2[i]=arr1[i]

print("Original array is:")
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
print()

print("New array is:")
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")
