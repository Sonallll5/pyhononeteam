num=153
b=0
while num !=0:
    d=num%10
    if d>b:
        b=d
    num//=10
print(b)
