a=[1,2,3,4,5,6,1,3,2,5,2,3,4]
b=[]
for i in a:
   if i not in b:
    b.append(i)
for i in b:
   c=0  
   for j in a:      
     if i==j:
       c+=1
print(i ,"in",c, "times")            
