from random import choice
from string import ascii_lowercase

class Cipher(object):
    def __init__(self, key=None):
        if key == None:
            self.key = ''.join(choice(ascii_lowercase) for _ in range(100))
        elif key.isalpha() and key.islower():
            self.key = key
        else:
            raise ValueError

    def encode(self, msg):
        ciphertext = ''
        for i, c in enumerate(msg.lower()):
            if c.isalpha():
                new_ord = ord(c) + ord(self.key[i % len(self.key)]) - ord('a')
                ciphertext += chr(new_ord - 26 if new_ord > ord('z') else new_ord)

        return ciphertext

    def decode(self, msg):
        plaintext = ''
        for i, c in enumerate(msg):
            new_ord = ord(c) - ord(self.key[i % len(self.key)]) + ord('a')
            plaintext += chr(new_ord + 26 if new_ord < ord('a') else new_ord)

        return plaintext

class Caesar(Cipher):
    def __init__(self):
        super().__init__('d')
