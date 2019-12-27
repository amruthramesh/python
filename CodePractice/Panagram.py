import string


def panagram(a):

    flag = False
    for i in string.ascii_lowercase:
        if i in a.lower():
            flag = True
            continue
        else:
            flag = False
            break
    return flag


a = 'The Quick brown Fox Jumps over a lazy dog'
b = 'Venkat'
result = panagram(b)
if result:
    print('It is a Panagram')
else:
    print('your word is not a panagram')