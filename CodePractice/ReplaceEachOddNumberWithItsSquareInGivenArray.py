
def square_of_odd_in_list(list):
    print('Before process',list)

    # list = [i**2 if i%2 !=0 else i for i in list]
    print(id(list))
    for ind, i in enumerate(list):

        if i%2 != 0:
            sq = i * i
            list[ind] = sq
    print (list)
    print('after process',list)



list = [1,2,3,6,4,7,5,9,10,20,13,55,44,19]
square_of_odd_in_list(list)



