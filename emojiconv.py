# Simple python program that convert keybord smileys to emoji

#first split the message into words
message = input(">")
words = message.split(' ')

#make dictionary for emoji

emojis = {
    ":)": "🙂",
    ":(": "😔"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
    
print(output)
