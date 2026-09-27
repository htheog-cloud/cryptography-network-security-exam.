ST001,John Doe,Electronics
ST002,Jane Doe,Telecommunication
ST003,Eric Smith,Networking
from cryptography.fernet import Fernet, InvalidToken
import hashlib
import os
import sys


def generate_key(key_file):
    """Generate an encryption key if it does not exist."""
    if not os.path.exists(key_file):
        key = Fernet.generate_key()

        with open(key_file, "wb") as file:
            file.write(key)

        print("Encryption key generated.")
    else:
        print("Existing encryption key found.")


def load_key(key_file):
    """Load and validate the encryption key."""
    try:
        with open(key_file, "rb") as file:
            key = file.read()

        Fernet(key)
        return key

    except FileNotFoundError:
        print("Error: Encryption key file was not found.")
        return None

    except (ValueError, TypeError):
        print("Error: Invalid encryption key.")
        return None


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        return None

    except PermissionError:
        print(f"Error: Permission denied for '{file_path}'.")
        return None


def encrypt_file(input_file, encrypted_file, key):
    """Encrypt the student record file."""
    try:
        with open(input_file, "rb") as file:
            original_data = file.read()

        encrypted_data = Fernet(key).encrypt(original_data)

        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)

        print(f"File encrypted successfully: {encrypted_file}")
        return True

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' was not found.")
        return False

    except PermissionError:
        print("Error: Permission denied while accessing the file.")
        return False


def decrypt_file(encrypted_file, decrypted_file, key):
    """Decrypt the encrypted file."""
    try:
        with open(encrypted_file, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = Fernet(key).decrypt(encrypted_data)

        with open(decrypted_file, "wb") as file:
            file.write(decrypted_data)

        print(f"File decrypted successfully: {decrypted_file}")
        return True

    except FileNotFoundError:
        print(f"Error: Encrypted file '{encrypted_file}' was not found.")
        return False

    except InvalidToken:
        print("Error: Decryption failed. File may be corrupted or key is invalid.")
        return False

    except PermissionError:
        print("Error: Permission denied while accessing the file.")
        return False


def verify_contents(original_file, decrypted_file):
    """Verify that decrypted contents match the original."""
    try:
        with open(original_file, "rb") as file:
            original_data = file.read()

        with open(decrypted_file, "rb") as file:
            decrypted_data = file.read()

        if original_data == decrypted_data:
            print("Verification successful: Decrypted contents match the original.")
            return True
        else:
            print("Verification failed: Decrypted contents do not match the original.")
            return False

    except FileNotFoundError:
        print("Error: Original or decrypted file was not found.")
        return False


def save_hash(hash_file, file_hash):
    """Save the original SHA-256 hash."""
    try:
        with open(hash_file, "w") as file:
            file.write(file_hash)

        print(f"Original SHA-256 hash saved to: {hash_file}")
        return True

    except PermissionError:
        print("Error: Permission denied while saving the hash.")
        return False


def check_file_integrity(file_path, hash_file):
    """Check whether the file has changed since the original hash was saved."""

    if not os.path.exists(hash_file):
        print("No original hash found.")
        return False

    try:
        with open(hash_file, "r") as file:
            original_hash = file.read().strip()

    except PermissionError:
        print("Error: Permission denied while reading the hash.")
        return False

    current_hash = calculate_hash(file_path)

    if current_hash is None:
        return False

    print("\nOriginal SHA-256:")
    print(original_hash)

    print("\nCurrent SHA-256:")
    print(current_hash)

    if current_hash == original_hash:
        print("\nIntegrity check: PASSED - File has not changed.")
        return True
    else:
        print("\nIntegrity check: FAILED - File has been changed.")
        return False


def main():

    if len(sys.argv) != 2:
        print("Invalid input.")
        print("Usage: python encryption_tool.py student_records.txt")
        return

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    # Key is stored outside the GitHub repository.
    project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    key_file = os.path.join(project_folder, "student_encryption.key")

    encrypted_file = input_file + ".encrypted"
    decrypted_file = input_file + ".decrypted"
    hash_file = input_file + ".sha256"

    # Generate or load encryption key.
    generate_key(key_file)

    key = load_key(key_file)

    if key is None:
        return

    # Calculate current SHA-256 hash.
    current_hash = calculate_hash(input_file)

    if current_hash is None:
        return

    print("\nCurrent SHA-256 hash:")
    print(current_hash)

    # Save the original hash only if it does not already exist.
    if not os.path.exists(hash_file):
        save_hash(hash_file, current_hash)
    else:
        print(f"Existing hash file found: {hash_file}")

    # Encrypt the file.
    if not encrypt_file(input_file, encrypted_file, key):
        return

    # Decrypt the file.
    if not decrypt_file(encrypted_file, decrypted_file, key):
        return

    # Verify decrypted contents.
    verify_contents(input_file, decrypted_file)

    # Check file integrity.
    print("\nChecking file integrity:")
    check_file_integrity(input_file, hash_file)


if __name__ == "__main__":
    main()

encryption_tool/student_records.txt
encryption_tool/student_records.txt.decrypted
encryption_tool/student_records.txt.sha256
