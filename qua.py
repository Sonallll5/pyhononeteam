a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
x=b**2-4*a*c
if x==0 :
    x1=-b/(2*a)
    print(x1)
elif x>0:
    x2=b+x**0.5/(2*a)
    x3=b-x**0.5/(2*a)
    print(x2,x3)
else:
    print("imgnary")
