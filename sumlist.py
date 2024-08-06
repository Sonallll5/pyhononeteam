limit = int(input("Enter the limit "))
m = []
n = []
s = []
for i in range(limit):
    l1 = int(input("Enter the element of list 1 "))
    l2 = int(input("Enter the element of list 2 "))
    m.append(l1)
    n.append(l2)
    s.append(l1+l2)

print(m)
print(n)
print(s)