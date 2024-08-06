n=input()
l=len(n)
n=int(n)
temp=n
sum=0
while n!=0:
    d=n%10
    sum=sum+d**l
    n//=10
if temp==sum:
    print("Arm")
else:
    print("not")