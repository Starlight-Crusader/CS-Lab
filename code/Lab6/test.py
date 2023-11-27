from cryptosystems import RSA, ElGamal
from Crypto.Hash import RIPEMD160

# MESSAGE

msg = "Arteom KALAMAGHIN"

decimal_str =  int(''.join(str(ord(char)) for char in msg))

hasher = RIPEMD160.new()
hasher.update(str.encode(str(decimal_str)))
hash_hex = hasher.hexdigest()
hash_dec = int(''.join(str(ord(char)) for char in hash_hex))

print("Intial message:\n", decimal_str, "->", hash_hex, "~", hash_dec)

cipher = 0

if cipher:
    print("RSA:")

    A = RSA()
    B = RSA()

    cryptogram = A.encrypt(msg, B.public_key)
    signed_cryptogram = A.sign(msg, cryptogram)

    print("Encrypted message:\n", cryptogram)
    print("Signature:\n", signed_cryptogram[1])
    print("Signature verification (signature ^ e mod n) - VALID:\n", pow(signed_cryptogram[1], A.public_key[1], A.public_key[0]))

    print("Verification result - VALID:", B.verify(signed_cryptogram, A.public_key))
else:
    print("ElGamal:")

    A = ElGamal()
    B = ElGamal()

    cryptogram = A.encrypt(msg, B.public_key)
    signed_cryptogram = A.sign(msg, cryptogram)

    print("Encrypted message:\n", cryptogram)
    print("Signature:\n", (signed_cryptogram[1], signed_cryptogram[2]))
    print("Signature verification - VALID:", B.verify(signed_cryptogram, A.public_key))