a=[1,2,3,4,5]
seclarge=0
for i in range(len(a)):
    if a[i]>seclarge:
        seclarge=a[i]
print (seclarge)
i=0
while(1):
    if a[i]!=seclarge:
        sbig=a[i]
        break
    i+=1
for i in range(i+1,len(a)):
    if a[i]<seclarge and a[i]>sbig:
        sbig=a[i]
print("big",seclarge)
print("sbig",sbig)



