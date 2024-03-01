def ceasar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if 'A' <= c <= 'Z':
            c_encoded = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= c <= 'z':
            c_encoded = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            c_encoded = c
        cipher_text += c_encoded
    return cipher_text