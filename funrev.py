def sum(n):
  sum=0
  while n!=0:
    d=n%10
    sum = sum+d
    n//=10
  return sum
   
print(sum(45345))


#using function and sum