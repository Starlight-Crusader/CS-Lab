class Cipher:
    msg = ''
    keys = []
    lang_alphabet = []
    map = []

    def reset(self):
        self.keys = []
        self.map = []

    def check_input(self, op):
        ret = False

        if not all(char in self.lang_alphabet for char in self.keys[0]):
            print('ERROR: Unknown character in the key - you are allowed to use only rom. alphabet letters!')
            ret = True

        if not all(char in self.lang_alphabet for char in self.msg):
            print('ERROR: Unknown character in the message - you are allowed to use only rom. alphabet letters!')
            ret = True

        if op not in ['enc', 'dec']:
            print('ERROR: Unknown operation - pick enc/dec!')
            ret = True

        return ret

    def format_input(self):
        pass

    def set_map(self):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass
