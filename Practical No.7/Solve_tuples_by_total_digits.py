#Solve tuples by total digits

list = [(11, 23, 45, 34), (34, 67), (323,), (78, 15, 73, 95), (60, 35)]

print("list:",list)
result = sorted(list, key = lambda tup : sum([len(str(ele)) for ele in tup ]))
print("The sorted tuples:",result)

