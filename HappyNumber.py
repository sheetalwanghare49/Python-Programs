#Check Whether Given Number is Happy Number or not
def HappyNumber(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum

num=int(input("Enter the Number:"))
result=num
while(result!=1 and result!=4):
    result=HappyNumber(result)
        
if(result==1):
    print("Given Number is Happy Number")
elif(result==4):
    print("Given Number is not Happy Number")
