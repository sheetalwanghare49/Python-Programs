#Program to print pattern of pyramid centre align

rows = int(input("Enter number of rows: "))
k=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k+=1
        
    k=0
    print()

rows = int(input("Enter the number of rows:"))  
k =2*rows-2 
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k-2   
    for j in range(0, i + 1):  
        print("* ", end="") 
    print("")  
