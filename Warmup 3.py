N=6
A=[[(i+j) for i in range(N)] for j in range(N)]
def double(A):
    B=[]
    for i in range(len(A)//2):
        B.append([])
        for j in range(len(A)//2):
            B[i].append(A[i][j])
        B[i]=B[i]*2
    B=B*2
    printMatrix(B)

def printMatrix(A):
    i=0
    while i<len(A):
        j=0
        while j<len(A[i]):
            print(A[i][j],' ',end='')
            j+=1
        i+=1
        print()
double(A)

#Runtime: big-Oh(n^2)
