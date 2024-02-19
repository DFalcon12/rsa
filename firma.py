import Crypto.Util.number
import hashlib

bits = 1024

pA = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("Este es el primo de Alice", pA ,"\n")
qA = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("qA", pA ,"\n")
pB = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("Este es el primo de Bob", pA ,"\n")
qB = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("qB", pA ,"\n")


nA = pA * qA
print("nA", nA, "\n")
nB = pB * qB
print("nB", nB, "\n")

phiA = ((pA - 1) * (qA - 1))
print("phiA", phiA, "\n")
phiB = ((pB - 1) * (qB - 1))
print("phiB", phiB, "\n")



