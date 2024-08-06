n=int(input())
i=1
while i<=n:
 if i%3==0 and i%5==0:
    print("fizz")
 elif i%3==0:
    print("buzz")
 elif i%5==0:
  print("Fizzbuzz")
 else:
   print(i)
 i+=1