def vigenere_decrypt(ciphertext,keyword):
    ciphertext=ciphertext.upper()
    keyword=keyword.upper()
    plaintext=""
    for i,char in enumerate(ciphertext):
        if char.isalpha():
            shift=ord(keyword[i%len(keyword)])-ord('A')
            plain_char=chr(((ord(char)-ord('A')-shift+26)%26)+ord('A'))
            plaintext+=plain_char
        else:
            plaintext+=char
    return plaintext
ciphertext=input("1: ")
keyword=input("2: ")
plaintext=vigenere_decrypt(ciphertext,keyword)
print(f"Decoded text: {plaintext}")
