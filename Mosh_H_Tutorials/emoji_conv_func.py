def emoji_cinverter(message):
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
    return output


message = input("> ")
print(emoji_cinverter(message))
