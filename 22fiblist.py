def fibonacci(n):
    a,b = 0,1
    #yield a
    print(b)
    for i in range(n-1):
        a, b = b, a + b
        print(b)
