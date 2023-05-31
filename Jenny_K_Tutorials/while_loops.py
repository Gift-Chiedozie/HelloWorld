"""# A simple count statement in while else block
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("in else block")
print("Out from loop")

# A simple count statement in a while if-else block
count = 1
while count <= 5:
    print(count)
    count += 1
    if count == 3:
        break  # Because this statement forcefully terminates the loop, the next block will not be printed
else:
    print("in else block")  # This statement will be passed
print("Out from loop")

# An assignment
count = 1
while count < 1:
    print(count)  # cannot print count since count is greater than one
    count += 1
else:  # since the condition is false, it comes into the else block and out
    print("in else block")
print("Out from loop")

# Sentinel values
number = int(input("enter a number (0  to quit): "))
while number != 0:
    print(number)
    number = int(input("enter a number (0  to quit): "))
else:
    print("in else block")
print("Out of else block")"""

# Another assignment
count = 0
num = int(input("Enter a number(0 to quit): "))
while num > 0:
    print(num)
    count += num
    num = int(input("Enter a number(0 to quit): "))
print(f"Total count is {count}")