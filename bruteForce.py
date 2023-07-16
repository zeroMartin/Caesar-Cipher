import os

text = input('Enter text you want to decrypt: ')
decrypted_list = []

def remove():
    if os.path.exists('decrypted_text.txt') == True:
        os.remove('decrypted_text.txt')



def bruteForce():
    s = 1
    
    while s <= 26:
        decrypted_text = ''
        for character in text:
            if character.isupper():
                decrypted_character = chr((ord(character) - s - 65) % 26 + 65)
                decrypted_text += decrypted_character
            elif character.islower():
                decrypted_character = chr((ord(character) - s - 97) % 26 + 97)
                decrypted_text += decrypted_character
        decrypted_list.append(decrypted_text)
        s += 1
    return decrypted_list


def write_file():
    with open('decrypted_text.txt', 'w') as f:
        for line in decrypted_list:
            f.write(line)
            f.write('\n')

remove()

decrypted_list = bruteForce()
print(decrypted_list)

write_file()
