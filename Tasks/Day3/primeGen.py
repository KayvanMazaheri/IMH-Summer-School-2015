import random
from primeFermat import isPrimeFermat

LARGE_PRIME = 29072553456409183479268752003825253455672839222789445223234915115682921921621182714164684048719891059149763352939888629001652768286998932224000980861127751097886364432307005283784155195197202827350411
def primeGen(N = 10 ** 4, RANGE = LARGE_PRIME):
	checkList = []
	for x in range(N):
		randomInt = random.randrange(RANGE, 2 * RANGE)
		if randomInt not in checkList:
			checkList.append(randomInt)

	primeList = []
	for number in checkList:
		if isPrimeFermat(number):
			primeList.append(number)

	return primeList
