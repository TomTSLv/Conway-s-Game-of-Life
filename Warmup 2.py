N=6
A=[[(i+j) for i in range(N)] for j in range(N)]
def printMatrix(A):
    i=0
    while i<len(A):
        j=0
        while j<len(A[i]):
            print(A[i][j],' ',end='')
            j+=1
        i+=1
        print()
def addone(A):
    for i in range(len(A)):
        A[i].append(0)
    A.append([0 for i in range(len(A[0]))])
    printMatrix(A)

addone(A)

#Runtime: big-Oh(n)
