def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryptedStringChars = []
    for character in string:
        currentAlphaIndex = alphabet.index(character)
        encryptedIndex = (currentAlphaIndex + key) % 26
        encryptedStringChars.append(alphabet[encryptedIndex])
    return "".join(encryptedStringChars)