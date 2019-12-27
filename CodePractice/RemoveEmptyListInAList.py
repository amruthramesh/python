def remove_empty_list(a):
    b = []
    for index, i in enumerate(a):
        if i:
            b.append(i)
    return b

    # print id(a)
    # a = [i for i in a if i]
    # print id(a)
    # return a




ye = [[2,4,5,6], [], [5,5,5,5], [], [55], ['amruth']]
result = remove_empty_list(ye)
print(result)