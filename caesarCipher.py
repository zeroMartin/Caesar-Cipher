import argparse

text_to_encrypt = 'martin'
text_to_decrypt = 'churPduwlq'

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--encrypt')
parser.add_argument('-s', '--shift', type=int)
args = parser.parse_args()


# Function to encrypt text
def caesar_encryption():
    
    encrypted_text = ''

    for character in args.encrypt:
        if character.isupper():
            encrypted_character = chr(((ord(character) + args.shift - 65) % 26) + 65)
            encrypted_text += encrypted_character
        elif character.islower():
            encrypted_character = chr(((ord(character) + args.shift - 97) % 26) + 97)
            encrypted_text += encrypted_character
    return encrypted_text

# Function to decrypt text
def caesar_decryption():
    s = 3
    decrypted_text = ''

    for character in text_to_decrypt:
        if character.isupper():
            decrypted_character = chr(((ord(character) - s - 65) % 26) + 65)
            decrypted_text += decrypted_character
        if character.islower():
            decrypted_character = chr(((ord(character) - s - 97) % 26) + 97)
            decrypted_text += decrypted_character
    return decrypted_text

encrypted_text = caesar_encryption()
print(encrypted_text)

decrypted_text = caesar_decryption()
print(decrypted_text)