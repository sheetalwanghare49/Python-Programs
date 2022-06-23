#Program to find maximum and minimum elements in tuple
tuple=(1,23,45,62,16,76,50,64,25)

n=len(tuple)
max=tuple[0]
min=tuple[0]
for i in range(1,n):
    if(tuple[i]>max):
       max=tuple[i]
    elif(tuple[i]<min):
        min=tuple[i]

print("Given tuple :", tuple)
print("Maximum element of tuple :", max)
print("Minimum element of tuple:", min)
