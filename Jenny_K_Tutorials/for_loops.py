number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
names = ["Jenny", "Mosh", "Chinwe", "ALX"]
squares = []
for name in names:
    print(name)
    if name == "Chinwe":
        print("Hey! It's me.")
        break
for i in number:
    square = i ** 2
    squares.append(square)
print("List of squares =",squares)