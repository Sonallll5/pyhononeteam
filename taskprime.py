s=10
e=20
for i in range(s,e):
  for j in range(2,i):
    if i%j==0:
      break
  else:
      print(i)