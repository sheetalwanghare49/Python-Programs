#Count unique values inside the list
list=['v','j','r','h','j','k','v','s']
print("Input list:",list)

list1=[]
count=0

for i in list:
    if i not in list1:
        count=count+1
        list1.append(i)

print("Output list:",list1)
print("Number of unique values are:",count)
