list = [5, 1, 3, 6, 8, 9, 1, 5, 7, 2, 2, 4]
uniques = []
for num in list:
    if num not in uniques:
        uniques.append(num)
print(uniques)