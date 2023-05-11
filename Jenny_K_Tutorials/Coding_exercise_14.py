# Calculates total average height from a list of heights
height = input("Use space to separate your list of numbers: ")
# 123 234 345 456 567 678 789 890
height_list = height.split()
count = 0
for height in height_list:
    count += 1
#print(count)
for i in range(count): # 0 1 2 3 4 5 6 7
   height_list[i] = int(height_list[i])
total = 0
for person in height_list:
    total += person
#print(total)
avg = total/count
print("Average height is: ", round(avg))
#print(height_list)
