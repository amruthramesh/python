def fact(x):
    f = 1
    for i in range(1, x+1):
        f = f * i

    return f


n = int(input('Enter the number for factorial : '))
factVal = fact(n)
print 'Factorial for {} is'.format(n), factVal




# Recurssive Factorial

def recurssiveFact(x):
    if x == 0:
        return 1
    else:
        return x * recurssiveFact(x - 1)

n = int(input('Enter the number for recurssive factorial : '))
factVal = fact(n)
print 'Recurssive Factorial for {} is'.format(n), factVal