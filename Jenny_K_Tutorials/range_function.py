a = range(10, 2, 2)  # Traverses the list by two-step size
for i in a:
    print(i)

a = range(15, 2, -3)  # i=15, j=2, k=-3
# i, i+k, i+2k, i+3k ... j-1
for i in a:
    print(i)

a = range(15, 0, -1)  # prints in reverse from 15 t0 1
# note that if the step size is not present, nothing will output on the screen
# because we can not scale from 15 to 0 in an ascending other
# therefore the need for a negative step size to tell that the other is in descending
for i in a:
    print(i)

a = range(-1, -10, -1)  # prints out negative numbers from -1 to -9
for i in a:
    print(i)

# Function that calculates the sum of a range of numbers
count = 0
for i in range(1, 101):
    count += i
print(count)
