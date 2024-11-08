from collections import Counter

def character_frequency(text):
    # Calculate the frequency of each character
    frequency = Counter(text)
    # Sort by order of appearance in the text
    sorted_chars = sorted(frequency.items(), key=lambda x: text.index(x[0]))
    # Print each character and its frequency
    for char, count in sorted_chars:
        print(f"'{char}': {count}")

def caesar_decrypt(ciphertext, key):
    #do this
    '''caeser_decrypt(ciphertext, key)'''
    decrypted_text = []
    
    # Loop through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the starting point based on case
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the decrypted character
            decrypted_char = chr((ord(char) - start - key) % 26 + start)
            decrypted_text.append(decrypted_char)
        else:
            # If it's not a letter, just append it as is
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

def atbash_decrypt(ciphertext):
    '''atbash_decrypt(ciphertext)'''
    decrypted_text = []
    
    # Loop through each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():
            # Determine the starting point based on case
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the decrypted character
            decrypted_char = chr(start + (25 - (ord(char) - start)))
            decrypted_text.append(decrypted_char)
        else:
            # If it's not a letter, just append it as is
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)


## all part of affine decrypt
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Modular inverse doesn't exist

def affine_decrypt(ciphertext, a, b):
    '''affine_decrypt(ciphertext, a, b) ... a and b are coprime'''
    
    # m is the size of the alphabet
    m = 26
    
    # Check if 'a' and 'm' are coprime
    if gcd(a, m) != 1:
        raise ValueError(f"a must be coprime to {m}, but gcd({a}, {m}) = {gcd(a, m)}")
    
    # Find the modular inverse of a
    a_inv = mod_inverse(a, m)
    
    decrypted_text = []
    
    for char in ciphertext:
        if char.isalpha():
            # Determine the starting point based on case
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the decrypted character
            x = ord(char) - start
            decrypted_char = chr((a_inv * (x - b)) % m + start)
            decrypted_text.append(decrypted_char)
        else:
            # If it's not a letter, just append it as is
            decrypted_text.append(char)

    return ''.join(decrypted_text)

## ending of affine decrypt

def vigenere_decrypt(ciphertext, keyword):
    '''vigenere_decrypt(ciphertext, keyword)  ... keyword is prolly a word'''
    decrypted_text = []
    keyword_repeated = []

    # Repeat the keyword to match the length of the ciphertext
    keyword_length = len(keyword)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            keyword_repeated.append(keyword[i % keyword_length].lower())
        else:
            keyword_repeated.append(ciphertext[i])  # Preserve non-alpha characters

    # Decrypt each character
    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():
            shift = ord(k) - ord('a')  # Calculate the shift based on keyword
            start = ord('A') if c.isupper() else ord('a')
            # Decrypt the character
            decrypted_char = chr((ord(c) - start - shift) % 26 + start)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(c)  # Preserve non-alpha characters

    return ''.join(decrypted_text)

## start of playfair cipher
def create_playfair_matrix(keyword):
    matrix = []
    used_chars = set()
    keyword = ''.join(filter(str.isalpha, keyword)).upper().replace('J', 'I')

    # Add unique characters from the keyword to the matrix
    for char in keyword:
        if char not in used_chars:
            used_chars.add(char)
            matrix.append(char)

    # Add the remaining letters of the alphabet
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            used_chars.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]  # 5x5 matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def playfair_decrypt(ciphertext, keyword):
    '''playfair_decrypt(ciphertext, keyword) ... keyword is prolly a word'''
    matrix = create_playfair_matrix(keyword)
    decrypted_text = []

    # Prepare ciphertext (group into pairs)
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    if len(pairs[-1]) == 1:  # If last pair is single letter, append a filler
        pairs[-1] += 'X'

    for pair in pairs:
        first, second = pair[0], pair[1]
        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        if row1 == row2:  # Same row
            decrypted_text.append(matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            decrypted_text.append(matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle swap
            decrypted_text.append(matrix[row1][col2])
            decrypted_text.append(matrix[row2][col1])

    return ''.join(decrypted_text)

## End of playfair cipher




