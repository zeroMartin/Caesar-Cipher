text = 'pduwlq'

decrypted_list = []

def bruteForce():
    s = 1
    
    while s <= 26:
        decrypted_text = ''
        for character in text:
            decrypted_character = chr((ord(character) - s - 97) % 26 +97)
            decrypted_text += decrypted_character
        decrypted_list.append(decrypted_text)
        s += 1
    return decrypted_list

decrypted_list = bruteForce()
print(decrypted_list)

