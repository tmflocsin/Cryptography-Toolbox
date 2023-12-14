import math
import string

main = string.ascii_lowercase


def caesar_encryption(text, s):
    # Cipher(n) = De-cipher(26-n)
    result = ""  # empty string
    for char in text:
        if (char.isupper()):  # if the text[i] is in upper case
            result += chr((ord(char) - ord('A') + s) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + s) % 26 + ord('a'))
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result


def caesar_decryption(text, s):
    return caesar_encryption(text, -s)


def columnar_encryption(s, key):
    # to remove repeated alphabets in key
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
    k = ""
    for i in temp:
        k += i
    print("\nThe key used for encryption is: ", k)

    # ceil is used to adjust the count of
    # rows according to length of message
    b = math.ceil(len(s) / len(k))

    # if b is less than length of key, then it will not form square matrix when
    # length of meessage not equal to rowsize*columnsize of square matrix
    if (b < len(k)):
        b = b + (len(k) - b)
    # if b is greater than length of key, then it will not from a
    # square matrix, but if less then length of key, we have to add padding

    arr = [['_' for i in range(len(k))]
           for j in range(b)]
    i = 0
    j = 0
    # arranging the message into matrix
    for h in range(len(s)):
        arr[i][j] = s[h]
        j += 1
        if (j > len(k) - 1):
            j = 0
            i += 1
    print("The message matrix is: ")
    for i in arr:
        print(i)

    cipher_text = ""
    # To get indices as the key numbers instead of alphabets in the key, according
    # to algorithm, for appending the elementsof matrix formed earlier, column wise.
    kk = sorted(k)

    for i in kk:
        # gives the column index
        h = k.index(i)
        for j in range(len(arr)):
            cipher_text += arr[j][h]
    return cipher_text


def columnar_decryption(s, key):
    # to remove repeated alphabets in key
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
    k = ""
    for i in temp:
        k += i
    print("\nThe key used for encryption is: ", k)

    arr = [['' for i in range(len(k))]
           for j in range(int(len(s) / len(k)))]

    # To get indices as the key numbers instead of alphabets in the key, according
    # to algorithm, for appending the elementsof matrix formed earlier, column wise.
    kk = sorted(k)

    d = 0
    # arranging the cipher message into matrix
    # to get the same matrix as in encryption
    for i in kk:
        h = k.index(i)
        for j in range(len(k)):
            arr[j][h] = s[d]
            d += 1

    print("The message matrix is: ")
    for i in arr:
        print(i)

    # the plain text
    plain_text = ""
    for i in arr:
        for j in i:
            plain_text += j
    return plain_text


def vigenere_encryption(plain_text, key):
    index = 0
    cipher_text = ""

    # convert into lower case
    plain_text = plain_text.lower()
    key = key.lower()

    # For generating key, the given keyword is repeated
    # in a circular manner until it matches the length of
    # the plain text.
    for c in plain_text:
        if c in main:
            # to get the number corresponding to the alphabet
            off = ord(key[index]) - ord('a')

            # implementing algo logic here
            encrypt_num = (ord(c) - ord('a') + off) % 26
            encrypt = chr(encrypt_num + ord('a'))

            # adding into cipher text to get the encrypted message
            cipher_text += encrypt

            # for cyclic rotation in generating key from keyword
            index = (index + 1) % len(key)
        # to not to change spaces or any other special
        # characters in their positions
        else:
            cipher_text += c

    return cipher_text


def vigenere_decryption(cipher_text, key):
    index = 0
    plain_text = ""

    # convert into lower case
    cipher_text = cipher_text.lower()
    key = key.lower()

    for c in cipher_text:
        if c in main:
            # to get the number corresponding to the alphabet
            off = ord(key[index]) - ord('a')

            positive_off = 26 - off
            decrypt = chr((ord(c) - ord('a') + positive_off) % 26 + ord('a'))

            # adding into plain text to get the decrypted messag
            plain_text += decrypt

            # for cyclic rotation in generating key from keyword
            index = (index + 1) % len(key)
        else:
            plain_text += c

    return plain_text


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
    print("Please select an action: ")
    print("-" * 25)
    print("| 1. Encrypt Message\t|")
    print("| 2. Decrypt Message\t|")
    print("| 3. Exit         \t|")
    print("-" * 25)


def show_techniques():
    print("\nPlease select an encryption technique: ")
    print("-" * 33)
    print("| 1. Caesar \t\t\t|")
    print("| 2. Columnar Transposition\t|")
    print("| 3. Vigenere \t\t\t|")
    print("| 4. Back\t\t\t|")
    print("-" * 33)


while True:
    show_menu()
    action = input("Enter your choice: ")

    if action == "1":
        show_techniques()
        enc_choice = input("Enter your choice: ")

        if enc_choice == "1":
            word = str(input("\nEnter the message: "))
            k = int(input("Enter the shift: "))
            result = caesar_encryption(word, k)
            print("Text Encrypted~")
            save_to_file(result)

        elif enc_choice == "2":
            msg = input("\nEnter the message: ")
            key = input("Enter the key in alphabets: ")
            print("Text Encrypted~")
            result = columnar_encryption(msg, key)
            save_to_file(result)

        elif enc_choice == "3":
            plain_text = input("\nEnter the message: ")
            key = input("Enter the key: ")
            result = vigenere_encryption(plain_text, key)
            print("Text Encrypted~")
            save_to_file(result)

        elif enc_choice == "4":
            show_menu()

        else:
            print("Invalid number. Please try again.")

    elif action == "2":
        show_techniques()
        dec_choice = input("Enter your choice: ")

        if dec_choice == "1":
            word = str(input("\nEnter the message to be decrypted: "))
            d = int(input("Enter the shift: "))
            result = caesar_decryption(word, d)
            print("Text Decrypted~")
            save_to_file(result)

        elif dec_choice == "2":
            msg = input("\nEnter the message to be decrypted: ")
            key = input("Enter the key in alphabets: ")
            print("Text Decrypted~")
            result = columnar_decryption(msg, key)
            save_to_file(result)

        elif dec_choice == "3":
            cipher_text = input("\nEnter the message to be decrypted: ")
            key = input("Enter the key for decryption: ")
            result = vigenere_decryption(cipher_text, key)
            print("Text Decrypted~")
            save_to_file(result)

        elif dec_choice == "4":
            show_menu()

        else:
            print("Invalid number. Please try again.")

    elif action == "3":
        break

    else:
        print("Invalid number. Please try again.")