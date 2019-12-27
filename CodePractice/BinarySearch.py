
def binary_search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid+1
    return False


list = [5,7,44,6,8,9]
x = int(input('Enter the number to search : '))
result = binary_search(list, x)
if result:
    print('Number found')
else:
    print('Number not found')