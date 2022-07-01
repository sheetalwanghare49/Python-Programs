#Python program to replace words from dictionary
dict={1:"Apple",3:"Orange",5:"Pineapple",4:"Watermelon",2:"Banana"}
key=int(input("Enter the key to replace value:"))
value=str(input("Enter new value:"))
for i in dict.keys():
    if(i==key):
        dict[i]=value
print("Dictionary after replacement:",dict)
