import random, sympy

# p - some big prime (the following value was proposed in the assignment text)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

# g - the generator (also was provided, so called 'primitive root' of p)

g = 2

print()

# d - A's secret (have to be smaller than p, but let it be smaller than 100 to ease computations)

d = random.randint(2, 100)
print("d (A's secret) = random.randint(2, p-1) =")
print(d, end="\n\n")

# e - A's public

e = pow(g, d, p)
print("e (A's public) = g^d mod p =")
print(e, end="\n\n")

# So A's public key is (p, g, e) and private key is (p, d)

a_pub = (p, g, e)
a_pr = (p, d)

print("A's public key - (p, g, e):")
print(a_pub, end="\n\n")

print("A's private key - (p, d):")
print(a_pr, end="\n\n")


# The requested message was "Nume Prenume" ...
# I converted it in accordance with ASCII decimal representations

msg = "Nume Prenume"
m = int(''.join(str(ord(char)) for char in msg))
print("Initial message ~ 'Nume Prenume' ~", m, end="\n\n")

# k - B's secret (have to be smaller than p, but let it be smaller than 100 to ease computations)

k = random.randint(2, 100)
print("k (B's secret) = random.randint(2, 100) =")
print(k, end="\n\n")

# Compute B1 and B2 so that (B1, B2) will be our cryptogram:
# ~ B1 = g^k mod p;
# ~ B2 = m * e^k mod p

B1 = pow(a_pub[1], k, a_pub[0])
B2 = pow((m * pow(a_pub[2], k)), 1, a_pub[0])

c = (B1, B2)

print("c - cryptogram of the message - (B1, B2):")
print(c, end="\n\n")

# m = dec(c) = B2 * (B1^d)^(-1) mod p

dec_c = pow(c[1] * sympy.mod_inverse(pow(c[0], a_pr[1]), a_pr[0]), 1, a_pr[0])
print("dec(c) == m -", dec_c == m, "and is:")
print(dec_c, end="\n\n")