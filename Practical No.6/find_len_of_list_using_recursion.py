#Program to find len of list using recursion
len=0
def length(a):
    global len
    if a:
        len = len + 1
        length(a[1:])
    return len

a=[1,2,4,5,7,9,0,4]
print("List:",a)
len=length(a)
print("The length of list is ",len)

