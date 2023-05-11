list = [5, 1, 3, 6, 8, 9, 1, 5, 7, 2, 2, 4]
list2 = ["James", "John", "Orange", "SweetPotatoes", "Orange", "Peter", "John"]
uniques = []
for num in list:
    if num not in uniques:
        uniques.append(num)
#print(uniques)
for item in list2:
    if item not in uniques:
        uniques.append(item)
print(uniques)