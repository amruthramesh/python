
# def fibo_series(n):
#     a, b = 0,1
#     print a,b,
#
#     for i in range(2, n):
#         c = a + b
#         if c < n:
#             a = b
#             b = c
#             print c,


def fuc(n):
    a,b = 0,1
    while a < n:
        print a,
        a,b = b,a+b




x = int(input('Enter the range of fibonnaci : '))
fuc(x)