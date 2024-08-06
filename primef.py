limit = int(input("Enter a limit: "))
for i in range(2, limit + 1):
    if limit % i == 0:
        break
    else:
        print(i)

    

     