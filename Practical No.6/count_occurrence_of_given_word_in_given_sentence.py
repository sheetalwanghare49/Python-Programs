#Program to count occurrence of given word in a given sentence
sen=str(input("Enter the sentence:"))
word=str(input("Enter a word:"))
arr=[]
count=0
arr=sen.split(" ")
for i in range(0,len(arr)):
    if(word==arr[i]):
        count=count+1
print("count of the word:",count)
