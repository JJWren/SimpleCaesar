# SimpleCaesar
This is an importable class structure for making and decrypting a Caesar Cipher.
Contains encryption and decryption methods.

Running the `main.py` file will give an example encryption/decryption process:
```py
    cipher = CaesarCipher()
    cipher.get_key()  # Allows user input to set the desire Caesar key

    message = "Please do not throw sausage pizza away."

    encrypted_text = cipher.encrypt_message(message)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = cipher.decrypt_message(encrypted_text)
    print(f"Decrypted text: {decrypted_text}")
```
