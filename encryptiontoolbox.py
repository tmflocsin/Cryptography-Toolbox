from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import secrets
import string

ALPHABET_LENGTH = 26
UPPER_A_ASCII = ord('A')
LOWER_A_ASCII = ord('a')
ASCII_PRINTABLE_START = 33
ASCII_PRINTABLE_END = 126

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def substitution_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += key[alphabet.index(char.lower())].upper()
            else:
                result += key[alphabet.index(char)]
        else:
            result += char
    return result

def save_to_file(result):
    file_name = input("\nEnter the output file name: ")
    with open(file_name, 'w') as file:
        file.write(result)
    print(f"Result saved to {file_name}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None

def show_menu():
    print("\n\nWelcome to the Encryption Toolbox!")
    print("Please select an encryption technique:")
    print("-"*33)
    print("| 1. Caesar Cipher\t\t|")
    print("| 2. Substitution Cipher\t|")
    print("| 3. Vigenere Cipher\t\t|")
    print("| 4. Exit\t\t\t|")
    print("-"*33)

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        action = input("Enter 'e' or 'd': ")
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        if action == 'e':
            result = caesar_cipher(text, shift)
            print("Text Encrypted~")
            save_to_file(result)
        elif action == 'd':
            result = caesar_cipher(text, 26 - shift)
            print("Text Decrypted~")
            save_to_file(result)
        
    elif choice == "2":
        text = input("Enter the text to encrypt/decrypt: ")
        key = input("Enter the substitution key: ")
        encrypted = substitution_cipher(text, key)
        decrypted = substitution_cipher(encrypted, key)
        print("Encrypted text:", encrypted)
        print("Decrypted text:", decrypted)
        
    elif choice == "4":
        break
        
    else:
        print("Invalid number. Please try again.")
