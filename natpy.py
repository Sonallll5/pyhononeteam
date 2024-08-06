n=int(input())
r=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(r,end=" ")
        r+=2
    print()

