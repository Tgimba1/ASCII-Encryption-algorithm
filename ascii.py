def reverse_engineer_password(encrypted_password):
    # The first character remains unchanged
    original_password = encrypted_password[0]
    
    # Decrypt the rest of the password by subtracting the position index from the ASCII value
    for i in range(1, len(encrypted_password)):
        original_password += chr(ord(encrypted_password[i]) - i)
    
    return original_password

# Example usage
encrypted_password = input("Enter the encrypted password: ")
decrypted_password = reverse_engineer_password(encrypted_password)
print(f"Original password: {decrypted_password}")
