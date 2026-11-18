#Accept the string from user and count the vowels from it.

str = input("Enter String: ")

count = str.count('a') + str.count('e') + str.count('i') + str.count('o') + str.count('u')

print("Number of vowels:", count)
