#Transpose of a matrix
A=[[3,5,6],[8,7,1],[1,6,4]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i]=A[i][j]
    for r in result:
        print(r)
