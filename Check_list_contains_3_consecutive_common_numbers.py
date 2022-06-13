#To check if the list contains 3 consecutive common elements
list = [6,4,2,1,7,7,7,9,0]
print("list =",list)
size = len(list)

for i in range(size - 2):
    if list[i] == list[i + 1] and list[i + 1] == list[i + 2]:
        print("The 3 consecutive common element in list:",(list[i]))
