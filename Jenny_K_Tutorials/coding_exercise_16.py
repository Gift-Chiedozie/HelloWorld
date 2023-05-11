# Calculates the sum of even number from 1 to 100, including 1 & 100
count = 0
for i in range(1, 101):  #1, 2, 3, 4, 5 ... 100
    if i % 2 == 0:
        count += i
    print(i)
print(count)