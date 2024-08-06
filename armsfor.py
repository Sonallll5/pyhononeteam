n = input("Enter a number: ")
l = len(n)
n = int(n)
temp = n
sum = 0


for digit in str(n):
    sum += int(digit) ** l

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
