# Python program to compute the diff between 2 list
def list_diff(list1, list2):
    out = []
    for ele in list1:
        if not ele in list2:
            out.append(ele)
    return out

list1 = [11, 16, 21, 26, 31, 36, 41] 
list2 = [26, 41, 36,45,89] 

print("The difference between list1 and list 2:",list_diff(list1, list2))
print("The difference between list2 and list 1:",list_diff(list2, list1))
