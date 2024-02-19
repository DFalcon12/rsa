#Practica de Algoritmo RSA

import Crypto.Util.number

bits = 1024

#Obtener primos para A y B

pA = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("Este es el primo de Alice", pA ,"\n")
qA = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("qA", pA ,"\n")
pB = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("Este es el primo de Bob", pA ,"\n")
qB = Crypto.Util.number.getPrime(bits, randfunc = Crypto.Random.get_random_bytes)
print("qB", pA ,"\n")

#Llave publica

nA = pA * qA
print("nA", nA, "\n")
nB = pB * qB
print("nB", nB, "\n")

#Calcular el indicador de Euler Phi

phiA = ((pA - 1) * (qA - 1))
print("phiA", phiA, "\n")
phiB = ((pB - 1) * (qB - 1))
print("phiB", phiB, "\n")

#Numero de fermat
e = 65537
#Calcular las llave privadas
dA = Crypto.Util.number.inverse(e, phiA)
print("dA", dA , "\n")

dB = Crypto.Util.number.inverse(e, phiB)
print("dB", dB , "\n")

#Ciframos el mensaje
msg = 'Hola mundo'
print("Mensaje original: ", msg, "\n")
print("Longitud del mensaje en bytes es: ", len(msg.encode('utf-8')))

#Convertir el mensaje a numero
m = int.from_bytes(msg.encode('utf-8'), byteorder = 'big')
print("mensaje convertido en entero: ", m ,"\n")

#Ciframos el mensaje
c = pow(m,e,nB)
print("Mensaje cifrado: ", c, "\n")

#Desciframos el mensaje
des = pow(c, dB, nB)
print ("Mensaje descifrado: ", des, "\n")

#Convertir el mensaje a texto
msg_final = int.to_bytes(des, len(msg), byteorder = 'big').decode('utf-8')
print("Mensaje final: ", msg_final, "\n")