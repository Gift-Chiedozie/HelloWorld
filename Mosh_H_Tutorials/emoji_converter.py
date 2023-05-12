message = input("> ")
words = message.split(" ")  # splits message into separate words
emojis = {
    ":)": "😊",
    ";)": "😉",
    ":-D": "😁",
    ":-O": "😮",
    ":-(": "🙁",
    ";P": "😋",
    "=)": "😃"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)