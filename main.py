class CaesarCipher:
    '''Allows user to set a Caesar key and encrypt or decrypt a Caesar cipher based on the set key. Initial key value is set to 0.'''

    def __init__(self):
        self.ALPHABET: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_+-={}|[]\\:;\"'<>,.?/"
        self.key: int = 0

    def get_key(self):
        '''Set the Caesar Cipher key value.'''
        try:
            key: int = int(input("Input encryption/decryption key: "))
            self.key = key
        except ValueError as e:
            print(f"Key must be an integer: {e}")
            self.get_key()

    def encrypt_message(self, message: str) -> str:
        encrypted_message: str = ""
        for character in message:
            if character in self.ALPHABET:
                char_idx: int = self.ALPHABET.index(character)
                translated_idx: int = char_idx + self.key

                while translated_idx >= len(self.ALPHABET):
                    translated_idx -= len(self.ALPHABET)
                while translated_idx < 0:
                    translated_idx += len(self.ALPHABET)

                encrypted_message += self.ALPHABET[translated_idx]
            else:
                encrypted_message += character
        return encrypted_message

    def decrypt_message(self, message: str) -> str:
        decrypted_message: str = ""
        for character in message:
            if character in self.ALPHABET:
                char_idx: int = self.ALPHABET.index(character)
                translated_idx: int = char_idx - self.key

                while translated_idx >= len(self.ALPHABET):
                    translated_idx -= len(self.ALPHABET)
                while translated_idx < 0:
                    translated_idx += len(self.ALPHABET)

                decrypted_message += self.ALPHABET[translated_idx]
            else:
                decrypted_message += character
        return decrypted_message


if __name__ == "__main__":
    cipher = CaesarCipher()
    cipher.get_key()

    message = "Please do not throw sausage pizza away."

    encrypted_text = cipher.encrypt_message(message)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = cipher.decrypt_message(encrypted_text)
    print(f"Decrypted text: {decrypted_text}")
