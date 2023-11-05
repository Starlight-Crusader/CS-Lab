import random

# p - some big prime (the following value was proposed in the assignment text)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039

# a - the generator (also was provided)

a = 2

print()

# Pick a random private keys for Alice and Bob

pr_alice = random.randint(1, p)
pr_bob = random.randint(1, p)

print("Private key ~ (random.randint(1, p)) ~ Alice:")
print(pr_alice, end="\n\n")

print("Private key ~ (random.randint(1, p)) ~ Bob:")
print(pr_bob, end="\n\n")

# Compute the corresponding public keys

pub_alice = pow(a, pr_alice, p)
pub_bob = pow(a, pr_bob, p)

print("Public key ~ a^(pr_alice) mod p ~ Alice:")
print(pub_alice, end="\n\n")

print("Public key ~ a^(pr_bob) mod p ~ Bob:")
print(pub_alice, end="\n\n")

# Compute common secret k = pub_bob^pr_alice mod p = pub_alice^pr_bob mod p = (a^pr_alice)^pr_bob mod p

common_secret_alice = pow(pub_bob, pr_alice, p)
common_secret_bob = pow(pub_alice, pr_bob, p)

# Check the keys

print("Keys generated are identical -", common_secret_alice == common_secret_bob, f"are {pub_alice.bit_length()} bits in size and equal to:")
print(common_secret_alice, end="\n\n")