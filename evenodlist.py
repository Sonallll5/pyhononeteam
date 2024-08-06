o=[1,2,3,4,5,6,8,9]
e=[22,333,444,556,66,7,777,8]
o.extend(e)
e.clear()
for i in e:
    if i %2!=0:
       e.append(i)
       o.remove(i)
print(o)
print(e)