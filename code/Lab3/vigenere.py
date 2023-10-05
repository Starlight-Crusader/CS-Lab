from cipher import Cipher


class Vigenere(Cipher):
    def find_letter_id(self, letter):
        n = -1

        for i in range(len(self.lang_alphabet)):
            if self.lang_alphabet[i] == letter:
                n = i
                break

        return n

    def format_input(self):
        self.keys[0] = str.upper(self.keys[0])

        formated_msg = str.upper(self.msg)
        self.msg = formated_msg
        
        formated_msg = ''
        for char in self.msg:
            if char == ' ':
                continue
            else:
                formated_msg += char

        self.msg = formated_msg

        keystream = ''

        idx = 0
        for i in range(len(self.msg)):
            keystream += self.keys[0][idx]
            idx = (idx + 1) % len(self.keys[0])

        self.keys.append(keystream)

    def set_map(self):
        map = []
        n = len(self.lang_alphabet)

        for i in range(n):
            row = []
            for j in range(n):
                idx = (i + j) % n
                row.append(self.lang_alphabet[idx])

            map.append(row)

        self.map = map

    def encrypt(self):
        for l in range(len(self.msg)):
            j = self.find_letter_id(self.msg[l])
            i = self.find_letter_id(self.keys[1][l])

            self.msg = self.msg[:l] + self.map[i][j] + self.msg[l+1:]

    def decrypt(self):
        for l in range(len(self.msg)):
            i = self.find_letter_id(self.keys[1][l])

            for j in range(len(self.map[i])):
                if self.map[i][j] == self.msg[l]:
                    self.msg = self.msg[:l] + self.lang_alphabet[j] + self.msg[l+1:]
                    break
