import time
while True:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mode = input("Encrypt or decrypt ").lower()
    if mode != "decrypt" and mode != "encrypt":
        print("You did not enter a valid mode")
        continue
    stringToEncrypt = input("Enter message: ")
    stringToEncrypt = stringToEncrypt.upper()
    shiftAmount = int(input("Enter a key between 1-25 "))
    if mode == "decrypt":
        shiftAmount = -shiftAmount
    encryptedString = ""
    for currentCharacter in stringToEncrypt:
        position = alphabet.find(currentCharacter)
        newPosition = position + shiftAmount
        if currentCharacter in alphabet:
            encryptedString = encryptedString + alphabet[newPosition]
        else:
            encryptedString = encryptedString + currentCharacter
    print("Processing...")
    time.sleep(2)
    print("Message is", encryptedString)
