
def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list


list = [7,6,0,11,9,3,1]
result = bubble_sort(list)
print(result)