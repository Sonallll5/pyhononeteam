limit=int(input("Enter the limit"))
larg=[]
for i in range (limit):
    e=int(input())
    larg.append(e)
print(larg)
big=0
for j in range (limit):
    if larg[j]>big:
        big=larg[j]
print("largest:",big)