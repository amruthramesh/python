# Anonymous function

nums = [2,6,8,15,16,7,28]

# Filter the values from List
evennum = list(filter(lambda n : n%2==0, nums)) 
# Performs the operation on chunk of data
doubles = list(map(lambda n : n*2, evennum))
# Reduces the values based on the operation 
sum = reduce(lambda a,b : a+b, doubles)
print 'Filter is ', evennum
print 'Map is ', doubles
print 'Reduce is ', sum