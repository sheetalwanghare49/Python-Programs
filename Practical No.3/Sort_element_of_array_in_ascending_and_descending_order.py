#Sort elements in ascending and descending order

arr=[4,7,8,2,1,9]
temp=0

#print original array
print("Element in original array:")
for i in range(0,len(arr)):
    print(arr[i], end=" ")
print()

#print array in ascending order
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Elements of array arrange in Ascending order:")
for i in range(0,len(arr)):
    print(arr[i], end=" ")
print()

#print array in descending order
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]<arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Elements of array arrange in Descending order:")
for i in range(0,len(arr)):
    print(arr[i], end=" ")

    
