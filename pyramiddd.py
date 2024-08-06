limit=int(input())
for i in range(limit,0,-1 ):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 
for k in range(2,limit+1 ):
    for l in range(1,k+1):
        print(l,end=" ")
    print() 