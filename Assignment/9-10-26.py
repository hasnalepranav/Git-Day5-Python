#Print the table of odd number from 1 to 10
for num in range(1, 11):
    if num % 2 != 0:
        print("Table of", num)
        for i in range(1, 11):
            print(num, "x", i, "=", num * 1)
        print()
        
#Create a heterogenous list of numbers and names.Split the list from highest number.

heterogenous_list = [1, "Pranav", 2, "Prasad", 5, "Ayush", 4, "Gaurav"]
largest = max(x for x in heterogenous_list if isinstance(x, int)) # Find the largest number
index = heterogenous_list.index(largest) # Find the position of the largest number
list1 = heterogenous_list[:index] # Split the list
list2 = heterogenous_list[index:]
print(list1)
print(list2)

# Accept the name and check its palindrome

name = input("Enter a name:")
if name.lower() == name[::-1].lower():
    print(f"{name} is a palindrome.")
else:
    print(f"{name} is not a palindrome.")

#Print the sum of digits

num = int(input("Enter a number:"))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10
print(total)

# print following pattern
# *
# ##
# ***

n = 3
for i in range(1, n+1):
    if i % 2 != 0:
        print("*"*i)
    else:
        print("#"*i)
