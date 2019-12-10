
def count(lst):
    more = 0
    less = 0
    for i in lst:
        if len(i)>3:
            more += 1
        else:
            less += 1
    return more, less


lst = ['Amruth', 'dog', 'icecream', 'daddy', 'bike', 'it']
more, less = count(lst)

print 'Word length more than 3 is {} and Word length less than 3 is {}'.format(more, less)