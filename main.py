import random
from group import *

# Define parameters: 
#       generator:          g
#       prime:              p 
#       random private key: r
#       message:            m
#       Bob's public key:   bob_pk

g = 666
p = 6661
r = random.randrange(1, p)  # Generate random r in the range [1, p-1]
m = 2000  # Message to encrypt
bob_pk = 2227  # Bob's public key

# Create a group with modulus p
group = ModPowGroup(p)

print("Task 1")
# Encryption: Calculate c1 = g^r mod p and c2 = m * bob_pk^r mod p
c1 = group.Pow(g, r)  # c1 is the first part of the ciphertext
c2 = group.Compose(m, group.Pow(bob_pk, r))  # c2 is the second part of the ciphertext
print(f"Encrypted message, c1: {c1}, c2: {c2}")
print()


print("Task 2")
# Brute force to find Bob's private key (bob_sk) such that g^bob_sk = bob_pk
for i in range(1, p):
    if group.Pow(g, i) == bob_pk:  # Find the private key that matches Bob's public key
        bob_sk = i  # Bob's private key
        break

print("Bobs private key: ", bob_sk)

# Decryption: shared_secret = c1^bob_sk mod p
shared_secret = group.Pow(c1, bob_sk)  # Compute shared secret using c1 and bob_sk
shared_secret_inv = group.Inverse(shared_secret)  # Compute inverse of the shared secret

print("Shared secret: ", shared_secret)
print("Shared secret inverse: ", shared_secret_inv)

# Decrypt the original message: message = c2 * shared_secret_inv mod p
message = group.Compose(c2, shared_secret_inv)
print("Decrypted message: ", message)
print()

print("Task 3")
# Constant
k = 3
# Modify the second part of the ciphertext (c2)
modified_c2 = group.Compose(c2, k)  # Modify c2 by multiplying it with 3 (changes the content to "6000")
print(f"New encrypted message, c1: {c1}, c2: {modified_c2}")

# Decrypt the modified message
message = group.Compose(modified_c2, shared_secret_inv)
print("Decrypted modified message: ", message)
