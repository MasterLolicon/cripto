from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

dest=raw_input("Destino:\n1.Nidia\n2.Alice\n")

if(dest=="1"):
 #se obtiene la llave publica de nidia
 nidia=open("pubNidia.txt","r")
 pubKey=RSA.importKey(nidia.read())
 nidia.close()
 #print pubKey


elif(dest=="2"):
 #se obtiene la llave publica de alice
 alice=open("pubAlice.txt","r")
 pubKey=RSA.importKey(alice.read())
 alice.close()
 #print pubKey


#se obtiene la llave privada de bob
bob=open("privBob.txt")
privKey=RSA.importKey(bob.read())
bob.close()
#print privKey

#se abre el mensaje
msg=open("msg.txt","r")
mens=msg.read()
#print mens
msg.close()

#se genera el digesto
hash1=SHA.new(mens).hexdigest()
#print hash1

#otra forma de firma
firma=privKey.sign(hash1,123)
#print firma

#se cifra el mensaje con la llave publica
msg_ciph=pubKey.encrypt(mens,32)
#print "mensaje cifrado:\n"+str(msg_ciph)

#se guarda en el archivo
enc=open("../cf.txt","w")
enc.write(str(msg_ciph)+"\n-------------------------------\n"+str(firma))
enc.close()
print "mensaje cifrado\n"