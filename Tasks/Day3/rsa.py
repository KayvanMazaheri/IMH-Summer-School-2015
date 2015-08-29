
publicKey = (0, 0)
privateKey = 0

def __generate_phi__(p, q):
	phi = (p-1)*(q-1)
	return phi

def __find_e__(phi):
	return phi - 1

def __find_d__(e, phi):
	from inverse import inverse
	return inverse(e, phi)

def getPrivateKey():
	return privateKey

def getPublicKey():
	if publicKey == (0, 0):
		print("Keys not generated yet.")
	return publicKey

def generateKeys():
	from primeGen import primeGen
	primeList = primeGen(100, 100)
	
	p = primeList[0]
	q = primeList[1]

	n = p * q

	phi = __generate_phi__(p, q)

	e = __find_e__(phi)

	d = __find_d__(e, phi)

	privateKey = d 
	publicKey = (e, n)
	
	return publicKey

