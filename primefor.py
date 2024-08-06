#prime or not
limit = int(input("Enter the limit "))
prime = []
not_p = []
for i in range(limit):
    e = int(input("Element "))
    for j in range(2,e):
        if e%j==0:
            not_p.append(e)
            break
    else:
        prime.append(e)
print(prime)
print(not_p)