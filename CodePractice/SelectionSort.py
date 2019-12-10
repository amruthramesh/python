def selection_sort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i,len(list)):
            if list[j] < list[min]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

    return list



list = [99,88,77,66,55,44,33,11,22]
result = selection_sort(list)
print result