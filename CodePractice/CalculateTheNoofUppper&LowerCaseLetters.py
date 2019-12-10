def count_case(a):
    ucount, lcount = 0, 0
    for i in a:
        if i.isupper():
            ucount += 1
        elif i.islower():
            lcount += 1
        else:
            pass
    return ucount, lcount

a = "The Quick Brown"
upper, lower = count_case(a)
print upper, lower