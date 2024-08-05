import os

chars = " " + "}8u#stax%lBz1f)c5Dg2_k7&pyh4.bvw{n3m0[9@rqiA*Vd5-j!o+C"
charLetter = len(chars)

def encryption(plainText, key):
    cypherText = ""
    for letter in plainText:
        index = chars.find(letter)
        if index == -1:
            cypherText += letter
        else:
            newIndex = index + key
            if newIndex >= charLetter:
                newIndex -= charLetter
            cypherText += chars[newIndex]
    return cypherText

def decryption(cypherText, key):
    plainText = ""
    for letter in cypherText:
        index = chars.find(letter)
        if index == -1:
            plainText += letter
        else:
            newIndex = index - key
            if newIndex < 0:
                newIndex += charLetter
            plainText += chars[newIndex]
    return plainText

os.system("cls")
print("=======================================================")
print("\tWelcome To Text Encrypter And Decrypter")
print("=======================================================")
print("To Encrypt Text, Press 1")
print("To Decrypt Text, Press 2")
choice = int(input("Enter Your Choice: "))

# ENCRYPT
if choice == 1:
    print("******\t ENCRYPTION MODE SELECTED\t******")
    print()
    key = int(input("Enter Key (1 - 26) [Recommended: 7]: "))
    plainText = input("Enter Your Message To Encrypt: ")
    entText = encryption(plainText, key)
    print("==============================================================")
    print("Original Message: ", plainText)
    print("Encrypted Message: ", entText)
    print("==============================================================")

# DECRYPT
elif choice == 2:
    print("******\t DECRYPTION MODE SELECTED\t******")
    print()
    key = int(input("Enter Key (1 - 26) [Recommended: 7]: "))
    entText1 = input("Enter Your Message To Decrypt: ")
    decText = decryption(entText1, key)
    print("==============================================================")
    print("Encrypted Message: ", entText1)
    print("Decrypted Message: ", decText)
    print("==============================================================")

else:
    print("WRONG MODE SELECTED!")
