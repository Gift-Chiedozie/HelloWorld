# THE SIMPLE ONE
import random
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
          'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
          'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator!")
letter = int(input("How many letters would you like in your password? \n"))
symbol = int(input("How many symbols would you like in your password? \n"))
number = int(input("How many numbers would you like in your password? \n"))
password = ""
for i in range(1, letter + 1):
    char = random.choice(letters)
    password += char
for i in range(1, symbol + 1):
    char = random.choice(symbols)
    password += char
for i in range(1, numbers + 1):
    char = random.choice(numbers)
    password += char
print(password)

# THE HARD ONE
