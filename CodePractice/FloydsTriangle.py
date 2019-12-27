

x = int(input('Enter the range to print floyds triangle : '))
k = 1
for i in range(1, x+1):
    for j in range(1, i+1):
        print(k, end=''),
        k = k+1
    print(" ")
print("\n")

for i in range(1, x+1):
    for j in range(1, i+1):
        print('*', end= ''),
    print(" ")
print("\n")

