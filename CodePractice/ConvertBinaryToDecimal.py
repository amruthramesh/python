def convertBinaryIntoDecimal(a):
    decimal, i, n = 0, 0, 0
    while a > 0:
        dec = a % 10
        decimal = decimal + dec * pow(2, i)
        a = a//10
        i += 1
    print decimal

x = int(input('Enter your Binary value : '))
convertBinaryIntoDecimal(x)


 
    




    