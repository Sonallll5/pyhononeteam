limit = int(input("Enter a limit: "))

for i in range(1, limit + 1):
    for j in range(1, limit + 1):
        print((i * j), end=" ")
    print()
