#Python program to find tuples which have all elements divisible by k

tuple=[(1,4,5),(34,65,76),(2,4,6)]
print("The given tuple is:", tuple)
K=2
print("The value of k:", K)
ans = [sub for sub in tuple if all(ele % K == 0 for ele in sub)]
  
print("Elements divisible by k:" + str(ans))
