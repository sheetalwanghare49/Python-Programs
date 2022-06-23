#Program to count the occurrence of each word in a given sentence
string = str(input("Enter any sentence:"))

arr=[]
arr=string.split(" ")
i=0
count=0
print("Sentence is:")
print(string)
print("occurrence of each word:")
while(i<len(arr)):
    count=0
    for j in arr:
        if arr[i]==j:
            count=count+1
    print(arr[i],":",count)
    i=i+1
