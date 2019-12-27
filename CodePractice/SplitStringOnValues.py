
# To calculate the nuber of rows to print
def calculate_split_val(str):
    for i in range(2,len(str)+1):
        if (len(str) % i == 0):
            return i
        else:
            continue

# Split the string based on the rows
def split_string(str, n):
    if (len(str) > 1):
        for i in range(0, len(str), n):
            print(str[i:i+n], end=' ')
            print()
    else:
        return str

string = str(input('Enter the string to split : '))
n = calculate_split_val(string)
split_string(string, n)
