#Print largest and smallest element in array
arr=[23,45,74,58,12,34,90]
max=arr[0]
min=arr[0]

for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
    if arr[i]>max:
        max=arr[i]
print("Largest element in array:",max)
print("Smallest element in array:",min)
