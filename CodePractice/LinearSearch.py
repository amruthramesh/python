
def linearSearch(list, n):
    for i in list:
        if i == n :
            return True
    return False


list = [3,7,5,6,9,8,23]
x = int(input('Enter the number to search : '))
result = linearSearch(list, x)
if result:
    print('Number found')
else:
    print('Number not found')