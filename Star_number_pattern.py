# Program to print number and pattern

for i in range (1,5):
    for j in range (1,i+1):
        if (j<i):
            print( i,"*"  , end =" ")    
        else:
            print (i)                            
    print()

for i in range (4,0,-1):
    for j in range (1,i+1):
        if (j<i):
            print( i,"*"  , end =" ")
        else:
            print (i)
    print()
