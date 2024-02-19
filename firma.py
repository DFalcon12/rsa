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

e = 65537

dA = Crypto.Util.number.inverse(e, phiA)
print("dA", dA , "\n")

dB = Crypto.Util.number.inverse(e, phiB)
print("dB", dB , "\n")

msg = 'Hola mundo'
print("Mensaje original: ", msg, "\n")
print("Longitud del mensaje en bytes es: ", len(msg.encode('utf-8')))

m = int.from_bytes(msg.encode('utf-8'), byteorder = 'big')
print("mensaje convertido en entero: ", m ,"\n")

c = pow(m,e,nB)
print("Mensaje cifrado: ", c, "\n")

des = pow(c, dB, nB)
print ("Mensaje descifrado: ", des, "\n")

msg_final = int.to_bytes(des, len(msg), byteorder = 'big').decode('utf-8')
print("Mensaje final: ", msg_final, "\n")

hashed_msg = hashlib.sha256(b'Hola mundo')
print(f'\nhashed_msg: {hashed_msg}')

mssg = int.from_bytes(hashed_msg.digest(), byteorder='big')
sA = pow(mssg, dA, nA)
print(f'Firma de alice: {sA}')

firma = pow(sA, e, nA)
print(f'Mensaje recibido de bob: {firma}')

if firma == mssg:
    print('Si hay firma')
else:
    print('Error')

