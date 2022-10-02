LASTNAME = "Parsa"

def encode(msg, key):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    alphabet.extend(alphabet)
    count = 0
    word = ""
    key = key * 100
    for i in msg:
        if i == " ":
            word = word + " "
        else:
            letter = alphabet.index(i) + alphabet.index(key[count])
            count = count + 1
            word = word + alphabet[letter]
    print(word)
