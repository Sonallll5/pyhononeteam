n=int(input())
s=0
temp=n
i=1
while i<n:
   if n%i==0:
    s=s+i
   i+=1 
if temp==s:
    print("perfect")
else:
   print("not")