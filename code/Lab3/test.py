from playfair import Playfair
from vigenere import Vigenere


repin = True

cipher = Vigenere()

rom_alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
rom_alphabet.remove('J')
    
rom_alphabet.insert(rom_alphabet.index('A')+1, 'Ă')
rom_alphabet.insert(rom_alphabet.index('Ă')+1, 'Â')
rom_alphabet.insert(rom_alphabet.index('I')+1, 'Î')
rom_alphabet.insert(rom_alphabet.index('S')+1, 'Ș')
rom_alphabet.insert(rom_alphabet.index('T')+1, 'Ț')

cipher.lang_alphabet = rom_alphabet

while repin:
    print("====================")

    cipher.keys.append(input('Insert the key : '))
    cipher.msg = input('Insert the message : ')
    option = input('Pick the operation (enc/dec) : ')
    cipher.format_input()

    repin = cipher.check_input(option)

cipher.set_map()

if option == 'enc':
    cipher.encrypt()
elif option == 'dec':
    cipher.decrypt()

print(cipher.msg)
