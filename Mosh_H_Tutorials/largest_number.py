#Prints the largest nunber in a list of numbers
list = [2, 48, 6, 89, 30, -10, 7]
max = list[0]
for num in list:
    if num > max:
        max = num
print(max)