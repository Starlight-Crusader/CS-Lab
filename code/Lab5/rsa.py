import sympy
from Crypto.Util.number import getPrime

print()

# p1, p2: Two random prime numbers of size 1024 bits each

p1 = getPrime(1024)
print("p1 (" + str(p1.bit_length()) +"b) - a random prime =")
print(p1, end="\n\n")

p2 = getPrime(1024)
print("p2 (" + str(p2.bit_length()) +"b) - a random prime =")
print(p2, end="\n\n")

# Product - 2048 bits

n = p1 * p2
print("n (" + str(n.bit_length()) +"b) = p1 * p2 =")
print(n, end="\n\n")

# Phi(n) ...

phi_n = (p1 - 1) * (p2 - 1)
print("Phi(n) = (p1 - 1) * (p2 -1) =")
print(phi_n, end="\n\n")

# e - the public exponent: a small odd number that shares no common factor with n (I've decided to pick some prime)
# d - the private exponent: mod. inverse of e

e = None
d = None

for p in list(sympy.primerange(1, 1000)):
    if n % p > 0:
        try:
            e = p
            d = sympy.mod_inverse(e, phi_n)
        except:
            continue

        break

print("e - a small odd num. that shares no common factor with n (I've decided to pick some prime) =")
print(e, end="\n\n")

print("d - mod. inverse of e =")
print(d, end="\n\n")

# The requested message was "Nume Prenume" ...
# I converted it in accordance with ASCII decimal representations

msg = "Nume Prenume"
m = int(''.join(str(ord(char)) for char in msg))
print("Initial message ~ 'Nume Prenume' ~", m, end="\n\n")

# enc(m, pub) - m^pub.e mod pub.n / dec(c, priv) - c^priv.d mod priv
# * pub.n = priv.n = n

c = pow(m, e, n)
m = pow(c, d, n)

print("enc(m) = ", c)
print("dec(c) = ", m)