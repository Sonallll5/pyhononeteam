a=str(input("Enter a string"))
r=''
for i in range(len(a)):
    if i%2==0:
        r+=a[i].upper()
    else:
        r+=a[i].lower()
print(r)
