#Check Whether Given Number is Disarium Number or not
num=str(input("Enter the Number:"))
length=len(num)
value=int(num)

rem=0
sum=0
num=int(num)
for i in range(length):
    rem=num%10
    sum=sum+(rem**length)
    num=num//10
    length=length-1

if(value==sum):
    print("Given Number is Disarium Number")
else:
    print("Given Number is not Disarium Number")
