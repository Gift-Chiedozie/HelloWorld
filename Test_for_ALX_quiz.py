"""a = [1, 2, 3]
b = a[:]
b[0] = 5
print(b)
print(a)
if a == b:
    print("A is equal to B")
elif a is b:
    print("A is B")
else:
    print("A is not B neither is it equal to B")"""

"""for word in "Jenny Khatri":
    print(word)"""

"""for number in range(20):
    if number % 3 == 0:
        print(number)

for fruit in ["banana", "apple", "quince"]:
    print("I like to eat " + fruit + "s!")"""

"""numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in range(len(numbers)): #the len funtion determines the length of the list first. Therefore, its legth = the range output 
    numbers[index] = numbers[index]**2
    print("Expo to numbers = ", numbers[index])"""

"""x = 'foo'
y = x
print(x) # foo
y += 'bar'
print(x) # foo
print("print '" + y + "' too")"""

'''a = 89
b = a + 1
if a is b:
    print("Yes")
else:
    print("No")'''

def copy_list(l):
    for x in l:
        return l[:]

copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)