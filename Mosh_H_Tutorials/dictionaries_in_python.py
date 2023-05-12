# Function that requests phone number from user in number and then prints the number back in words
digits = {
    "1": "One",
    "2": "Two" ,
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
Phone_No = input("Input Phone number: ")
lettered = []
for item in Phone_No:
    lettered += [digits.get(item, "!")]
print(lettered)