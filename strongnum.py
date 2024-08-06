num=int(input("number"))
temp=num
sum=0
while num!=0:
  d=num%10 
  f=1
  while d>1:
    f=f*d
    d-=1
    sum=sum+f
    num//=10
if sum==temp:
    print("yes")
else:
     print("no")