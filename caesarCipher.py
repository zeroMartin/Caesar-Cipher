text_to_encrypt = 'martin'
text_to_decrypt = 'pduwlq'

def caesar_encryption():
    s = 3
    encrypted_text = ''

    for character in text_to_encrypt:
        encrypted_character = chr(((ord(character) + s - 97) % 26) + 97)
        encrypted_text += encrypted_character
    return encrypted_text

def caesar_decryption():
    s = 3
    decrypted_text = ''

    for character in text_to_decrypt:
        decrypted_character = chr(((ord(character) - s - 97) % 26) + 97)
        decrypted_text += decrypted_character
    return decrypted_text

encrypted_text = caesar_encryption()
print(encrypted_text)

decrypted_text = caesar_decryption()
print(decrypted_text)