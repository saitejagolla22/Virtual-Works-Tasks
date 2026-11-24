
from cryptography.fernet import Fernet, InvalidToken
import os

# Generate a secret key
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Secret key generated successfully!")


# Load the secret key
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Secret key not found! Generate a key first.")
        return None


# Encrypt a file
def encrypt_file(filename):
    key = load_key()

    if key is None:
        return

    if not os.path.isfile(filename):
        print("File not found!")
        return

    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    output_file = filename + ".encrypted"

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")
    print("Encrypted file:", output_file)


# Decrypt a file
def decrypt_file(filename):
    key = load_key()

    if key is None:
        return

    if not os.path.isfile(filename):
        print("Encrypted file not found!")
        return

    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        output_file = filename.replace(
            ".encrypted", ".restored"
        )

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")
        print("Restored file:", output_file)

    except InvalidToken:
        print("Decryption failed! Invalid key or corrupted file.")


# Main menu
while True:

    print("\n===== FILE PROTECTION UTILITY =====")
    print("1. Generate Secret Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        filename = input("Enter file name: ")
        encrypt_file(filename)

    elif choice == "3":
        filename = input("Enter encrypted file name: ")
        decrypt_file(filename)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
