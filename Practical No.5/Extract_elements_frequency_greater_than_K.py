#Extract elements with frequency greater than K
list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
print("The original list : " + str(list))

K = 2
print("K=2")
res = []
for i in list:
	freq = list.count(i)
	if freq > K and i not in res:
		res.append(i)
		
print("The required elements : " + str(res))
