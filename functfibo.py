def fib(d):
    a = 0
    b = 1
    if d == 1:
        print(a)
    elif d == 2:
        print(a, b)
    else:
        print("Fibonacci series:")
        print(a)
        print(b)
        while d > 2:
            c = a + b
            a = b
            b = c
            print(c)
            d -= 1
print(fib(5))

