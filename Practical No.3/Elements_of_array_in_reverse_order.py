#Print elements of array in reverse order
arr=[6,8,9,7,5]

print("Original array is:")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print()
    
print("Array in reverse order is:")
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")
