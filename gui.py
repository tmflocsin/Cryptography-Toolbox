import tkinter as tk
from tkinter import ttk

def caesar_encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decryption(text, shift):
    return caesar_encryption(text, -shift)

def save_to_file(result, file_name):
    with open(file_name, 'w') as file:
        file.write(result)
    print(f"Result saved to {file_name}")

class EncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("Encryption Toolbox")

        self.tabControl = ttk.Notebook(master)

        self.caesar_tab = ttk.Frame(self.tabControl)
        self.columnar_tab = ttk.Frame(self.tabControl)
        self.vigenere_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.caesar_tab, text="Caesar Cipher")
        self.tabControl.add(self.columnar_tab, text="Columnar Transposition")
        self.tabControl.add(self.vigenere_tab, text="Vigenere Cipher")

        self.tabControl.pack(expand=1, fill="both")

        self.create_caesar_tab()
        # self.create_columnar_tab()  # Add this function for Columnar Transposition
        # self.create_vigenere_tab()  # Add this function for Vigenere Cipher

    def create_caesar_tab(self):
        label = tk.Label(self.caesar_tab, text="Enter the message:")
        label.pack()

        self.caesar_input = tk.Entry(self.caesar_tab)
        self.caesar_input.pack()

        label = tk.Label(self.caesar_tab, text="Enter the shift value:")
        label.pack()

        self.caesar_shift = tk.Entry(self.caesar_tab)
        self.caesar_shift.pack()

        encrypt_button = tk.Button(self.caesar_tab, text="Encrypt", command=self.caesar_encrypt)
        encrypt_button.pack()

        decrypt_button = tk.Button(self.caesar_tab, text="Decrypt", command=self.caesar_decrypt)
        decrypt_button.pack()

        self.caesar_result_label = tk.Label(self.caesar_tab, text="")
        self.caesar_result_label.pack()

    def caesar_encrypt(self):
        input_text = self.caesar_input.get()
        shift_value = int(self.caesar_shift.get())
        result = caesar_encryption(input_text, shift_value)
        self.caesar_result_label.config(text=f"Encrypted: {result}")
        save_to_file(result, "caesar_encrypted.txt")

    def caesar_decrypt(self):
        input_text = self.caesar_input.get()
        shift_value = int(self.caesar_shift.get())
        result = caesar_decryption(input_text, shift_value)
        self.caesar_result_label.config(text=f"Decrypted: {result}")
        save_to_file(result, "caesar_decrypted.txt")

# Main execution
root = tk.Tk()
app = EncryptionApp(root)
root.mainloop()
