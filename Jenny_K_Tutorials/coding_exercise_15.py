# Calculating maximum number in a list of numbers
numbers = input("Use comma to separate your numbers: ")
# 123 234 829 2573 2637 6392 917
number_list = numbers.split()
count = 0
for i in number_list:
    count += 1
for number in range(0, count): # 0 1 2 3 4 5 6
    number_list[number] = int(number_list[number])
print(f"The length of this list {number_list} is {count}")
max_num = number_list[0]  # 123
for num in number_list:  # 123 234 829 2573 2637 6392 917
    if num > max_num:
        max_num = num
print("Maximim number is = ", max_num)