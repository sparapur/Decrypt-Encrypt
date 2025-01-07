**Substitution Cipher Program**
A simple Python program that encrypts and decrypts text files using a substitution cipher.

Steps to Set Up:

- Create a commands.txt file with 4 lines:
Copykey.txt
encrypt
input.txt
output.txt
- Create a key.txt file with any 26-letter substitution alphabet
- Create your input.txt with the text you want to encrypt/decrypt

How It Works:

The program reads commands.txt to get:
Which key file to use
Whether to encrypt or decrypt
Input and output file locations


For encryption:

Replaces each letter in your text using your substitution alphabet
Uppercase letters stay uppercase, lowercase stay lowercase
Non-letters (spaces, numbers, punctuation) stay the same


For decryption:

Does the reverse process to get back the original text


Notes:

Your key must be 26 uppercase letters
Use "encrypt" or "decrypt" in commands.txt
The program preserves the original case of letters
All files must be in the same directory as the program
