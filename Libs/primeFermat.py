def isPrimeFermat( n , MAX_TRIES = 20):
  
  # Import required functions
  import random
  import time
  from exponentiation import fastExponentiationModulo

  # Initializing the random generator
  random.seed(time.time())

  for i in range(MAX_TRIES):
    randomInt = random.randrange(2, n)
    if fastExponentiationModulo(randomInt, n-1, n) != 1:
      return 0

  return 1

