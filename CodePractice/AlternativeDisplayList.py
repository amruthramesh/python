# Suppose
# a = [1,2,3,None,None]
# b = [4,5,3]
# Write a program to show output as [1,4,2,5,3,3]

def countAndAddNone(a, b):
    len_a, len_b = len(a), len(b)
    diff = abs(len(a) - len(b))
    if len(a) < len(b):
        for i in range(diff):
            a.append(None)
    elif len(b) < len(a):
        for i in range(diff):
            b.append(None)
    else:
        pass
    c = []
    for i in range(len(a)):
        if a[i] == None:
            if b[i] == None:
                continue
            else:
                c.append(b[i])
        elif b[i] == None:
            c.append(a[i])
        else:
            c.extend([a[i], b[i]])
            
    print c
            





list1 = [1,2,None]
list2 = [4,7,9,None,5,3]
countAndAddNone(list1, list2)