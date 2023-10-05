from cipher import Cipher


class Playfair(Cipher):
    def format_input(self):
        key = ''
        present_letters = []

        for char in str.upper(self.keys[0]):
            if char == ' ':
                continue

            if char not in present_letters:
                key += char
                present_letters.append(char)

        self.keys[0] = key

        formated_msg = str.upper(self.msg)
        self.msg = formated_msg
        
        formated_msg = ''
        for char in self.msg:
            if char == ' ':
                continue
            else:
                formated_msg += char

        self.msg = formated_msg

        formated_msg = ''

        idx = 0
        while idx < len(self.msg):
            try:
                if self.msg[idx] == self.msg[idx+1]:
                    formated_msg = formated_msg + self.msg[idx] + 'Z'
                    idx -= 1
                else:
                    formated_msg = formated_msg + self.msg[idx] + self.msg[idx+1]

                idx += 2
            except:
                formated_msg += self.msg[idx]
                idx += 1

        self.msg = formated_msg

        for idx in range(len(self.msg)):
            if self.msg[idx] == 'J':
                self.msg = self.msg[:idx] + 'I' + self.msg[idx+1:]

        if len(self.msg) % 2 != 0:
            self.msg += 'Z'
    
    def set_map(self):
        present_letters = []

        i, j = 0, 0
        row = []

        for char in [char for char in self.keys[0]] + self.lang_alphabet:
            if char not in present_letters:
                row.append(char)
                present_letters.append(char)

                j += 1
                if j > 4:
                    self.map.append(row)
                    
                    i += 1
                    j = 0
                    row = []

    def find_letter_id(self, letter):
        rn, cn = -1, -1

        for row in range(len(self.map)):
                for col in range(len(self.map[row])):
                    if self.map[row][col] == letter:
                        rn, cn = row, col
                        break

                if rn >= 0 and cn >= 0:
                    break

        return rn, cn

    def encrypt(self):
        idx = 0
        while idx < len(self.msg):
            r0, c0 = self.find_letter_id(self.msg[idx])
            r1, c1 = self.find_letter_id(self.msg[idx+1])

            if r0 == r1:
                c0 = (c0 + 1) % len(self.map[0])
                c1 = (c1 + 1) % len(self.map[0])
            elif c0 == c1:
                r0 = (r0 + 1) % len(self.map)
                r1 = (r1 + 1) % len(self.map)
            else:
                cr = c0 + 0
                c0 = c1
                c1 = cr

            self.msg = self.msg[:idx] + self.map[r0][c0] + self.msg[idx+1:]
            self.msg = self.msg[:idx+1] + self.map[r1][c1] + self.msg[idx+2:]

            idx += 2

    def decrypt(self):
        idx = 0
        while idx < len(self.msg):
            r0, c0 = self.find_letter_id(self.msg[idx])
            r1, c1 = self.find_letter_id(self.msg[idx+1])

            if r0 == r1:
                c0 = ((c0 - 1) + len(self.map[0])) % len(self.map[0])
                c1 = ((c1 - 1) + len(self.map[0])) % len(self.map[0])
            elif c0 == c1:
                r0 = ((r0 - 1) + len(self.map)) % len(self.map)
                r1 = ((r1 - 1) + len(self.map)) % len(self.map)
            else:
                cr = c0 + 0
                c0 = c1
                c1 = cr

            self.msg = self.msg[:idx] + self.map[r0][c0] + self.msg[idx+1:]
            self.msg = self.msg[:idx+1] + self.map[r1][c1] + self.msg[idx+2:]

            idx += 2

        orig_msg = ''
        for letter in self.msg:
            if letter != 'Z':
                orig_msg += letter

        self.msg = orig_msg
