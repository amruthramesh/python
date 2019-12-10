# Define a method to check whether the given vakue is binary or not


def checkBinaryOrNot(a):
    s = set(a)
    if s == {'0', '1'}:
        return True
    else:
        return False


get_number = raw_input('Enter your number : ')
result = checkBinaryOrNot(get_number)
if result:
    print('{} is a Binary'.format(get_number))
else:
    print('{} is not a binary'.format(get_number))