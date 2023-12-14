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
        master.title("Cute Encryption Toolbox")

        style = ttk.Style()
        style.configure("TFrame", background="#FFE4E1")
        style.configure("TLabel", background="#FFE4E1", font=('Arial', 12))
        style.configure("TButton", background="#FFD700", font=('Arial', 12))

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
        frame = ttk.Frame(self.caesar_tab, style="TFrame")
        frame.pack(padx=20, pady=20)

        label = ttk.Label(frame, text="Enter the message:", style="TLabel")
        label.grid(row=0, column=0, pady=5)

        self.caesar_input = ttk.Entry(frame, font=('Arial', 12))
        self.caesar_input.grid(row=0, column=1, pady=5)

        label = ttk.Label(frame, text="Enter the shift value:", style="TLabel")
        label.grid(row=1, column=0, pady=5)

        self.caesar_shift = ttk.Entry(frame, font=('Arial', 12))
        self.caesar_shift.grid(row=1, column=1, pady=5)

        encrypt_button = ttk.Button(frame, text="Encrypt", command=self.caesar_encrypt, style="TButton")
        encrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

        decrypt_button = ttk.Button(frame, text="Decrypt", command=self.caesar_decrypt, style="TButton")
        decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.caesar_result_label = ttk.Label(frame, text="", style="TLabel")
        self.caesar_result_label.grid(row=4, column=0, columnspan=2, pady=10)

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
