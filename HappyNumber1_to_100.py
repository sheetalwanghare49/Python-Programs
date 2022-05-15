#print Happy Number from 1 to 100
def isHappyNumber(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum
print("Happy Number from 1 to 100:")
for i in range(1,101):
    result=i
    while(result!=1 and result!=4):
         result=isHappyNumber(result)
    if(result==1):
        print(i)
       


    
    

