#Program for Perfect Number
num=int(input("Enter the number:"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("Given Number is Perfect Number")
else:
    print("Given Number is not Perfect Number")
