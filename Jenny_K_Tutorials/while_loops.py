# A simple count statement in while else block
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
        break
else:
    print("in else block")
print("Out from loop")

# An assignment
count = 1
while count < 1:
    print(count)  # cannot print count since count is greater than one
    count += 1
else:  # since the condition is false, it comes into the else block and out
    print("in else block")
print("Out from loop")