import numpy as np
import random

class AffineCipher():
    """
    An Affine Cipher object. The Affine Cipher is a special case of the Simple Substitution Cipher where the key is
    a permutation of the alphabet generated by the affine function (ax + b) % 26. The default key is the affine
    function (1x + 3) % 26, which is a classic Caesar Cipher with a shift of 3.
    """
    def __init__(self) -> None:
        """
        Creates an Affine Cipher object with the default key (1, 3), that is (1x + 3) % 26.

        Args:
            factor (int): The factor in the affine function.
            addend (int): The addend in the affine function.

        """   
        self.factor = 1
        self.addend = 3
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def set_key(self, factor: int, addend: int) -> None:
        """
        Sets the key used to generate the Affine Cipher.

        Args:
            factor (int): The factor in the affine function.
            addend (int): The addend in the affine function.

        Raises:
            ValueError: If the factor is not relatively prime to 26 or if the addend is not an integer.
        """

        # Check that the factor is relatively prime to 26
        if not greatest_common_divisor(factor, 26) == 1:
            raise ValueError("Factor must be relatively prime to 26.")
        # Check that the addend is an integer
        elif not isinstance(addend, int):
            raise ValueError("Addend must be an integer.")

        self.factor = factor
        self.addend = addend

    def get_key(self) -> tuple[int, int]:
        """
        Returns the key used to generate the Affine Cipher.

        Returns:
            Tuple[int, int]: The key used to generate the Affine Cipher.
        """
        return (self.factor, self.addend)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Affine Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.

        Raises:
            ValueError: If the plaintext is not a non-empty string.
        """

        # Check that the plaintext is a non-empty string
        if not isinstance(plaintext, str) or len(plaintext) == 0:
            raise ValueError("Plaintext must be a non-empty string.")
        
        # Initialize the ciphertext as an empty string
        ciphertext = ''

        # Iterate over each character in the plaintext, encrypting it and adding it to the ciphertext by
        # finding the index of the character in the plaintext alphabet, multiplying it by the factor, adding the addend,
        # and then finding the character in the ciphertext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in plaintext:
            if char.upper() in self.alphabet:
                ciphertext += self.alphabet[(self.alphabet.index(char.upper()) * self.factor + self.addend) % 26]
            else:
                ciphertext += char

        # Return the ciphertext
        return ciphertext
        
    
    def decrypt(self, plaintext: str) -> str:
        """
        Decrypts a message using the Affine Cipher.

        Args:
            plaintext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """

        # Check that the plaintext is a non-empty string
        if not isinstance(plaintext, str) or len(plaintext) == 0:
            raise ValueError("Plaintext must be a non-empty string.")
        
        # Initialize the ciphertext as an empty string
        ciphertext = ''

        # Find the multiplicative inverse of the factor
        inverse = find_modular_inverse(self.factor, 26)

        # Iterate over each character in the plaintext, decrypting it and adding it to the ciphertext by
        # finding the index of the character in the ciphertext alphabet, subtracting the addend, multiplying it by the
        # multiplicative inverse of the factor, and then finding the character in the plaintext alphabet at that index.
        # Characters not in the alphabet are left unchanged.
        for char in plaintext:
            if char.upper() in self.alphabet:
                ciphertext += self.alphabet[(self.alphabet.index(char.upper()) - self.addend) * inverse % 26]
            else:
                ciphertext += char

        # Return the ciphertext
        return ciphertext

class CaesarCipher():
    def __init__(self) -> None:
        """
        Creates a Caesar Cipher object capable of encrypting and decrypting messages using the Caesar Cipher.
        A Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter
        some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B
        would be replaced by E, and so on. The Caesar Cipher is named for Julius Caesar, who is purported to have used
        it to communicat with his generals. The default key is 3. 
        """

        # Initialize the alphabet and the shift
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 3

    def set_key(self, key: int) -> None:
        """
        Sets the shift used to generate the Caesar Cipher.

        Args:
            key (int): The key used to generate the Caesar Cipher.
        """
        self.key = key

    def get_key(self) -> int:
        """
        Gets the shift used to generate the Caesar Cipher.

        Returns:
            int: The shift used to generate the Caesar Cipher.
        """
        return self.key

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Caesar Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.
        """

        # Check that the plaintext is a non-empty string
        if not isinstance(plaintext, str) or len(plaintext) == 0:
            raise ValueError("Plaintext must be a non-empty string.")
        
        # Initialize the ciphertext as an empty string
        ciphertext = ''

        # Iterate over each character in the plaintext, encrypting it and adding it to the ciphertext by
        # finding the index of the character in the plaintext alphabet, adding the shift, and then finding
        # the character in the ciphertext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in plaintext:
            if char.upper() in self.alphabet:
                ciphertext += self.alphabet[(self.alphabet.index(char.upper()) + self.key) % 26]
            else:
                ciphertext += char
        
        # Return the ciphertext
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Caesar Cipher.
        
        Args:
            ciphertext (str): The message to decrypt.
        
        Returns:
            str: The decrypted message.
        """
        
        # Check that the ciphertext is a non-empty string
        if not isinstance(ciphertext, str) or len(ciphertext) == 0:
            raise ValueError("Ciphertext must be a non-empty string.")
        
        # Initialize the plaintext as an empty string
        plaintext = ''

        # Iterate over each character in the ciphertext, decrypting it and adding it to the plaintext by
        # finding the index of the character in the ciphertext alphabet, subtracting the shift, and then finding
        # the character in the plaintext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in ciphertext:
            if char.upper() in self.alphabet:
                plaintext += self.alphabet[(self.alphabet.index(char.upper()) - self.key) % 26]
            else:
                plaintext += char

        # Return the plaintext
        return plaintext
    
class HillCipher():
    def __init__(self) -> None:
        """
        Creates a Hill Cipher object.
        """
        self.key = None
        self.key_matrix = None
        self.inverse_key_matrix = None

    def get_key(self) -> str:
        """
        Returns the key used to generate the Hill Cipher.

        Returns:
            str: The key used to generate the Hill Cipher.
        """
        return self.key
    
    def set_key(self, key: np.array) -> None:
        """
        Sets the key used to generate the Hill Cipher.

        Args:
            key (np.array): The key used to generate the Hill Cipher.
        """
        self.key = key
        self.key_matrix = np.array([[ord(letter) - 65 for letter in row] for row in key])
        self.inverse_key_matrix = np.linalg.inv(self.key_matrix)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Hill Cipher.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """
        ciphertext = ''
        for i in range(0, len(plaintext), len(self.key_matrix)):
            plaintext_vector = np.array([[ord(letter) - 65] for letter in plaintext[i:i+len(self.key_matrix)]])
            ciphertext_vector = np.dot(self.key_matrix, plaintext_vector) % 26
            for letter in ciphertext_vector:
                ciphertext += chr(letter[0] + 65)
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Hill Cipher.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
        plaintext = ''
        for i in range(0, len(ciphertext), len(self.key_matrix)):
            ciphertext_vector = np.array([[ord(letter) - 65] for letter in ciphertext[i:i+len(self.key_matrix)]])
            plaintext_vector = np.dot(self.inverse_key_matrix, ciphertext_vector) % 26
            for letter in plaintext_vector:
                plaintext += chr(letter[0] + 65)
        return plaintext

class KeyedCaeserCipher():
    def __init__(self) -> None:
        """
        Creates a Keyed Caesar Cipher object capable of encrypting and decrypting messages using the Keyed Caesar Cipher.
        A Keyed Caesar Cipher is a special case of the Caesar Cipher that uses a key to generate a new alphabet. For
        example, if the key is 'ZEBRAS', then the alphabet would be 'ZEBRASCDFGHIJKLMNOPQTUVWXY'. The key is then used
        to encrypt and decrypt messages using the new alphabet.
        """
        self.key = None
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Keyed Caesar Cipher. Then converts the key to an alphabet by removing 
        duplicate letters and then appending the remaining letters of the alphabet in order. Then assigns the 
        resulting alphabet to the alphabet attribute.

        Args:
            key (str): The key to convert to an alphabet.

        Raises:
            ValueError: If the key is not a non-empty string.

        """
        # Check that the key is a non-empty string
        if not isinstance(key, str) or len(key) == 0:
            raise ValueError("Key must be a non-empty string.")
        
        # Assign the key to the key attribute for later retrieval or use
        self.key = key

        # Remove duplicate letters from the key
        key = ''.join(sorted(set(key), key=key.index))

        # Append the remaining letters of the alphabet in order
        for char in self.alphabet:
            if char not in key:
                key += char
        
        # Set the alphabet attribute to the key
        self.alphabet = key

    def get_key(self) -> str:
        """
        Returns the key used to generate the Keyed Caesar Cipher.

        Returns:
            str: The key used to generate the Keyed Caesar Cipher.
        """
        return self.key

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Keyed Caesar Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.
        """

        # Check that the plaintext is a non-empty string
        if not isinstance(plaintext, str) or len(plaintext) == 0:
            raise ValueError("Plaintext must be a non-empty string.")
        
        # Initialize the ciphertext as an empty string
        ciphertext = ''

        # Iterate over each character in the plaintext, encrypting it and adding it to the ciphertext by
        # finding the index of the character in the plaintext alphabet, adding the shift, and then finding
        # the character in the ciphertext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in plaintext:
            if char.upper() in self.alphabet:
                ciphertext += self.alphabet[(self.alphabet.index(char.upper()) + self.shift) % 26]
            else:
                ciphertext += char
        
        # Return the ciphertext
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Keyed Caesar Cipher.
        
        Args:
            ciphertext (str): The message to decrypt.
        
        Returns:
            str: The decrypted message.
        """
        
        # Check that the ciphertext is a non-empty string
        if not isinstance(ciphertext, str) or len(ciphertext) == 0:
            raise ValueError("Ciphertext must be a non-empty string.")
        
        # Initialize the plaintext as an empty string
        plaintext = ''

        # Iterate over each character in the ciphertext, decrypting it and adding it to the plaintext by
        # finding the index of the character in the ciphertext alphabet, subtracting the shift, and then finding
        # the character in the plaintext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in ciphertext:
            if char.upper() in self.alphabet:
                plaintext += self.alphabet[(self.alphabet.index(char.upper()) - self.shift) % 26]
            else:
                plaintext += char

        # Return the plaintext
        return plaintext

class SimpleSubstitutionCipher():
    def __init__(self) -> None:
        """
        Creates a Simple Substitution Cipher object with the default key 'XYZABCDEFGHIJKLMNOPQRSTUVW'. 
        The Caesar Cipher, the Atbash Cipher, the Affine Cipher, and the Keyed Caesar Cipher are all special cases of the
        Simple Substitution Cipher. Due to the nature of the Simple Substitution Cipher, the key must be a permutation
        of the alphabet. The key defaults to a classic Caesar Cipher with a shift of 3.
        """
        self.plaintext_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 'XYZABCDEFGHIJKLMNOPQRSTUVW'

    def set_random_key(self) -> None:
        """
        Sets the key to a random permutation of the alphabet.
        """
        self.key = ''.join(random.sample(self.alphabet, len(self.alphabet)))

    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Simple Substitution Cipher.

        Args:
            key (str): The key used to generate the Simple Substitution Cipher.

        Raises:
            ValueError: If the key is not a non-empty string or is not a permutation of the alphabet.
        """

        # Check that the key is a non-empty string
        if not isinstance(key, str) or len(key) == 0:
            raise ValueError("Key must be a non-empty string.")
        # Check that the key is a permutation of the alphabet
        elif sorted(key) != sorted(self.alphabet):
            raise ValueError("Key must be a permutation of the alphabet.")

        self.key = key

    def get_key(self) -> str:
        """
        Returns the key used to generate the Simple Substitution Cipher, which takes the form of a permutation of the alphabet.

        Returns:
            str: The key used to generate the Simple Substitution Cipher.
        """
        return self.key

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Simple Substitution Cipher. The key must be a permutation of the alphabet given
        as a string.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.

        Raises:
            ValueError: If the plaintext is not a non-empty string.

        """

        # Check that the plaintext is a non-empty string
        if not isinstance(plaintext, str) or len(plaintext) == 0:
            raise ValueError("Plaintext must be a non-empty string.")
        
        # Initialize the ciphertext as an empty string
        ciphertext = ''

        # Iterate over each character in the plaintext, encrypting it and adding it to the ciphertext by
        # finding the index of the character in the plaintext alphabet, and then finding character in the
        # ciphertext alphabet at that index. Characters not in the alphabet are left unchanged.
        for char in plaintext:
            if char.upper() in self.plaintext_alphabet:
                ciphertext += self.key[self.plaintext_alphabet.index(char.upper())]
            else:
                ciphertext += char

        # Return the ciphertext
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Simple Substitution Cipher.
        
        Args:
            ciphertext (str): The message to decrypt.
        
        Returns:
            str: The decrypted message.

        Raises:
            ValueError: If the ciphertext is not a non-empty string.

        """

        # Check that the ciphertext is a non-empty string
        if not isinstance(ciphertext, str) or len(ciphertext) == 0:
            raise ValueError("Ciphertext must be a non-empty string.")
        
        # Initialize the plaintext as an empty string
        plaintext = ''

        # Iterate over each character in the ciphertext, decrypting it and adding it to the plaintext by
        # finding the index of the character in the ciphertext alphabet, and then finding character in the
        # plaintext alphabet at that index. Characters not in the alphabet are left unchanged.
        for char in ciphertext:
            if char.upper() in self.key:
                plaintext += self.plaintext_alphabet[self.key.index(char.upper())]
            else:
                plaintext += char

        # Return the plaintext
        return plaintext
    
class VigenereCipher():
    def __init__(self) -> None:
        """
        Creates a Vigenere Cipher object with the specified key.

        Args:
            key (str): The key used to generate the Vigenere Cipher.
        """
    
    def get_key(self) -> str:
        """
        Returns the key used to generate the Vigenere Cipher.

        Returns:
            str: The key used to generate the Vigenere Cipher.
        """
        return self.key
    
    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Vigenere Cipher.

        Args:
            key (str): The key used to generate the Vigenere Cipher.
        """
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Vigenere Cipher.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Vigenere Cipher.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
    
class OneTimePad():
    def __init__(self, key: str) -> None:
        """
        Creates a One Time Pad object with the specified key.

        Args:
            key (str): The key used to generate the One Time Pad.
        """
        self.key = key
    
    def get_key(self) -> str:
        """
        Returns the key used to generate the One Time Pad.

        Returns:
            str: The key used to generate the One Time Pad.
        """
        return self.key
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the One Time Pad.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """

        
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the One Time Pad.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
        
    
class PlayfairCipher():
    def __init__(self) -> None:
        """
        Creates a Playfair Cipher object.
        """

    def get_key(self) -> str:
        """
        Returns the key used to generate the Playfair Cipher.

        Returns:
            str: The key used to generate the Playfair Cipher.
        """
        return self.key
    
    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Playfair Cipher.

        Args:
            key (str): The key used to generate the Playfair Cipher.
        """
        self.key = key

class KeyedColumnarTranspositionCipher():
    def __init__(self) -> None:
        """
        Creates a Keyed Columnar Transposition Cipher object.
        """

class ColumnarTranspositionCipher():
    def __init__(self) -> None:
        """
        Creates a Columnar Transposition Cipher object.
        """

        
    def set_key(self, key: list[int]) -> None:
        """
        Sets the key used to generate the Columnar Transposition Cipher.

        Args:
            key (list): The key used to generate the Columnar Transposition Cipher.
        """

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Columnar Transposition Cipher.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Columnar Transposition Cipher.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """

class RailFenceCipher():
    def __init__(self) -> None:
        """
        Creates a Rail Fence Cipher object. The Rail Fence Cipher is a transposition cipher that uses
        cyclic permutations to encrypt a message. The characters of the message are written in zigzag
        diagonals across a number of rows, and then read off in rows.

        The key, in this case, is the number of rows to use. Default is 3.
        """
        self.key = 3

    def set_key(self, key: int) -> None:
        """
        Sets the key used to generate the Rail Fence Cipher.

        Args:
            key (int): The key used to generate the Rail Fence Cipher.
        """
        self.key = key

    def get_key(self) -> int:
        """
        Returns the key used to generate the Rail Fence Cipher.

        Returns:
            int: The key used to generate the Rail Fence Cipher.
        """
        return self.key
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Rail Fence Cipher.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.

        Raises:
            ValueError: If the plaintext is not a non-empty string.
        """

        # Check if the plaintext is a non-empty string
        if not plaintext or not isinstance(plaintext, str):
            raise ValueError("Plaintext must be a non-empty string.")

        # Create a list of empty strings to represent the rows
        rows = ["" for _ in range(self.key)]

        # Create a variable to keep track of the row index
        row_index = 0

        # Create a variable to keep track of the direction of the zigzag
        direction = 1

        # Iterate through the plaintext
        for char in plaintext:
            # Add the current character to the row
            rows[row_index] += char

            # If we are at the top or bottom row, change the direction of the zigzag
            if row_index == 0 or row_index == self.key - 1:
                direction *= -1
            
            # Increment the row index
            row_index += direction
        
        # Return the ciphertext
        return "".join(rows)
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message encrypted with the Rail Fence Cipher.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        
        Raises:
            ValueError: If the ciphertext is not a non-empty string.
        """

        # Check if the ciphertext is a non-empty string
        if not ciphertext or not isinstance(ciphertext, str):
            raise ValueError("Ciphertext must be a non-empty string.")
        
        # Create a list of empty strings to represent the rows
        rows = ["" for _ in range(self.key)]

        # Create a variable to keep track of the row index
        row_index = 0

        # Create a variable to keep track of the direction of the zigzag
        direction = 1

        # Create a variable to keep track of the character index
        char_index = 0

        # Iterate through the ciphertext
        for char in ciphertext:
            # Add the current character to the row
            rows[row_index] += char

            # If we are at the top or bottom row, change the direction of the zigzag
            if row_index == 0 or row_index == self.key - 1:
                direction *= -1
            
            # Increment the row index
            row_index += direction

class AtBashCipher(AffineCipher):
    def __init__(self) -> None:
        """
        Creates an AtBash Cipher object. The AtBash Cipher is a special case of the Affine Cipher with a = 25 and b = 25.
        It is a monoalphabetic substitution cipher that is its own inverse that originated in the Hebrew alphabet.
        It is one of the earliest known ciphers and is even used in the Hebrew Bible in the Book of Jeremiah.
        """
        self.key = (25, 25)
    

class DoubleColumnarTransposition():
    def __init__(self) -> None:
        pass

class ADFGXCipher():
    def __init__(self) -> None:
        """
        Creates an ADFGX Cipher object.
        """
