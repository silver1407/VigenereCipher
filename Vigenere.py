# Create a Vigenere cipher
# Author: Jared Guthrie
# Date: 5/14/2022

# Vigenere Encryption
#Formula: (key[i] + plaintext[i]) % 26
def encryption(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr((((ord(key[i % len(key)]) + ord(plaintext[i])) % 26) + 65))
    return ciphertext

#Vigenere Decryption
#Formula: (cipertext[i] - key[i]) % 26
def decryption(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr((((ord(ciphertext[i]) - ord(key[i % len(key)])) % 26) + 65))
    return plaintext

#Main
def main():
    plaintext = input("Enter a message to encrypt: ")
    key = input("Enter a key to encrypt with: ")
    ciphertext = encryption(plaintext, key)
    print("Encrypted Message: ", ciphertext)
    plaintext = decryption(ciphertext, key)
    print("Decrypted Message: ", plaintext)

#Run
if __name__ == "__main__":
    main()