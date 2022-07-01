#Write telephone directory of 10 students using dictionary and perform operation
def star():
    for i in range(0,50):
        print("*",end=' ')
    print('\n')
tel_dir={'Tanvi':9112974690,'Aarti':9112799815,'Sheetal':9326213813,'Gauri':8767503578,'Akanksha':8856919915,'Payal':9321580934,'Sahil':9321565412,'Pravina':9892863191,'Khushi':9284784863,'Pranjal':9856734567}
print("Telephone Directory is:",tel_dir)

#A) finding value-key:value

key=str(input("Enter key to find value:"))
value=int()
for i in tel_dir.keys():
    if i == key:
        print("Telephone Number of given key is:",tel_dir[i])
star()
#B) replacing value-key:new key
key=str(input("Enter the key to find value:"))
value=int(input("Enter new value:"))

for i in tel_dir.keys():
    if i==key:
        tel_dir[i]=value
print("Dictionary after replacement:",tel_dir)
star()

#C) replacing key value - delete key - insert new value
num=int(input("Enter the Telephone number:"))
name=str(input("Enter new key:"))
for key,value in tel_dir.items():
    if num == value:
        old_key=key
tel_dir[name]=tel_dir.pop(old_key)
print("Dictionary after replacing key:value : ",tel_dir)

            

