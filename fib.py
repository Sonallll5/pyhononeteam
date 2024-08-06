limit = int(input("Enter your limit: "))
a=0
b=1
if limit==1:
    print(a)
elif limit==2:
    print(a,b)
else:
    print("fibonacci series....")
    print(a)
    print(b)
    while limit>2:
        c=a+b
        a=b
        b=c
        print(c)
        limit-=1



