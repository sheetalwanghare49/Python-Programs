#Print Disarium Number from 1 to 100
def disarium(num):
    rem=0
    sum=0
    val=num
    length=len(str(num))
    for i in range(length):
        rem=num%10
        sum=sum+(rem**length)
        num=num//10
        length=length-1
    if(val==sum):
        print(val)
print("Disarium Number from 1 to 100:")
for i in range(1,101):
    disarium(i)
