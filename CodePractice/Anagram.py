
def anagram(str1, str2):
    if len(str1) == len(str2):
        if set(str1) == set(str2):
            return True
    return False

str1 = raw_input('Enter first string : ')
str2 = raw_input('Enter second string : ')

result = anagram(str1, str2)
if result:
    print('Your word is an Anagram')
else:
    print('Your word is not an Anagram')