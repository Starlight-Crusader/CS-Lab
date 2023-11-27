from sympy import mod_inverse
from Crypto.Util.number import getPrime
from sympy import randprime
from random import randint
from math import gcd
from Crypto.Hash import RIPEMD160

def square_and_multiply(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus

    return result


class RSA:

    def __init__(self):
        p1 = getPrime(1536)
        p2 = getPrime(1536)

        self.n = p1 * p2
        self.phi_n = (p1 - 1) * (p2 - 1)

        self.e = self.generate_pub_exp()
        self.d = self.generate_private_key()

        self.public_key = (self.n, self.e)
        self.private_key = (self.d)

    def generate_pub_exp(self):
        e = 3
        while gcd(e, self.phi_n) > 1 or e % 2 == 0:
            e += 1

        return e

    def generate_private_key(self):
        return mod_inverse(self.e, self.phi_n)

    def encrypt(self, msg, reciever_public_key):
        decimal_str =  int(''.join(str(ord(char)) for char in msg))
        y = pow(decimal_str, reciever_public_key[1], reciever_public_key[0])
        return y
    
    def decrypt(self, y):
        x = pow(y, self.private_key, self.public_key[0])
        return x
    
    def sign(self, msg, transmission):
        decimal_str =  int(''.join(str(ord(char)) for char in msg))

        hasher = RIPEMD160.new()
        hasher.update(str.encode(str(decimal_str)))
        hash_hex = hasher.hexdigest()
        hash_dec = int(''.join(str(ord(char)) for char in hash_hex))

        return (transmission, pow(hash_dec, self.private_key, self.public_key[0]))
    
    def verify(self, transmission, sender_public_key):
        x = self.decrypt(transmission[0])
        s = pow(transmission[1], sender_public_key[1], sender_public_key[0])

        hasher = RIPEMD160.new()
        hasher.update(str.encode(str(x)))
        hash_hex = hasher.hexdigest()
        hash_dec = int(''.join(str(ord(char)) for char in hash_hex))

        return hash_dec == s

class ElGamal:

    def __init__(self):
        self.p = getPrime(3072)
        self.a = 2
        self.z = randint(2, self.p - 2)

        self.b = pow(self.a, self.z, self.p)

        self.public_key = (self.p, self.a, self.b)
        self.private_key = (self.z)

    def encrypt(self, msg, reciever_public_key):
        decimal_str =  int(''.join(str(ord(char)) for char in msg))

        i = randint(2, reciever_public_key[0] - 2)
        kE = pow(reciever_public_key[1], i, reciever_public_key[0])
        kM = pow(reciever_public_key[2], i, reciever_public_key[0])

        y = pow(decimal_str * kM, 1, reciever_public_key[0])

        return (kE, y)
    
    def decrypt(self, transmission):
        kM = pow(transmission[0][0], self.private_key, self.public_key[0])
        x = pow(transmission[0][1] * mod_inverse(kM, self.public_key[0]), 1, self.public_key[0])
        return x
    
    def sign(self, msg, transmission):
        decimal_str =  int(''.join(str(ord(char)) for char in msg))

        k = self.generate_k()
        r = pow(self.public_key[1], k, self.public_key[0])

        hasher = RIPEMD160.new()
        hasher.update(str.encode(str(decimal_str)))
        hash_hex = hasher.hexdigest()
        hash_dec = int(''.join(str(ord(char)) for char in hash_hex))

        s = (mod_inverse(k, self.public_key[0] - 1) * (hash_dec - self.private_key * r)) % (self.public_key[0] - 1)

        return (transmission, r, s)
    
    def verify(self, transmission, sender_public_key):
        x = self.decrypt(transmission)

        hasher = RIPEMD160.new()
        hasher.update(str.encode(str(x)))
        hash_hex = hasher.hexdigest()
        hash_dec = int(''.join(str(ord(char)) for char in hash_hex))

        p1 = pow(sender_public_key[2], transmission[1], sender_public_key[0])
        p2 = pow(transmission[1], transmission[2], sender_public_key[0])
        v1 = (p1 * p2) % sender_public_key[0]

        v2 = pow(sender_public_key[1], hash_dec, sender_public_key[0])

        print("v1 = v2 =\n", v2)

        return v1 % sender_public_key[0] == v2 % sender_public_key[0]
    
    def generate_k(self):
        k = randint(2, self.p - 1)
        while gcd(k, self.p - 1) > 1:
            k += 1

        return k
