#Check Whether Given Number is Harshad Number or not
num=int(input("Enter the Number:"))
rem=0
sum=0
n=num
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10

if(n%sum==0):
    print("Given Number is Harshad Number")
else:
    print("Given Number is not Harshad Number")
