# i = 1
# while i<5:
#     print "Amruth ",i
#     i += 1


# x = int(raw_input("Enter the number "))

# for y in range(2, x//2):
#     if (x % y) == 0:
#         print "Your number is not a prime number"
#         break
# else:
#     print "Your number is prime number"        
# import sys
# for j in range(4):
#     for i in range(4):
#         print("@ ",end="")
#     print()

import array

values = array.array('i', [2,3,4,5])
for i in values:
    if i==2:
        values[i]=7
        
    print i      
      

