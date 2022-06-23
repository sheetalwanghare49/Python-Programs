#print Pronic Numbers from 1 to 100
def PronicNumber(num):
    flag=0

    for j in range(num+1):
        if((j*(j+1))==num):
            flag=1
            break
    return flag

print("Pronic Numbers from 1 to 100:")
for i in range(1,101):
    if(PronicNumber(i)==1):
        print(i)
        
