def fact(n):
    if n==0:
        return "no result"
    elif n==1:
        return 1
    else:
        return n+fact(n-1)
s=fact(5)
print(s)
