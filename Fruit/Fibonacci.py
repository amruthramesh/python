def fibo(n):
    a, b = 0, 1
    lst = [a,b]
    for i in range(2, n):
        c = a + b
        if c <100:
            a = b
            b = c
            lst.append(c)
    return lst



n = int(input('Enter the number for fibonacci : '))
result = fibo(n)
print 'Fibonacci series for {} is'.format(n), result