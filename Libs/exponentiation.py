def fastExponentiation( base , power ):
  
  # Handling Base cases
  if power == 0:
    return 1
  if power == 1:
    return base


  # recursive call

  childAnswer = fastExponentiation(base, power // 2)
  childAnswer = childAnswer * childAnswer;

  # if power is odd
  if power % 2:
    childAnswer = childAnswer * base

  return childAnswer


def repeatedMultiplication( base, power ):

  result = 1

  for i in range(power):
    result *= base

  return result



def fastExponentiationModulo( base , power , modulo ):
  
  # Handling Base cases
  if power == 0:
    return 1
  if power == 1:
    return base


  # recursive call

  childAnswer = fastExponentiationModulo(base, power // 2, modulo)
  childAnswer = (childAnswer * childAnswer ) % modulo;

  # if power is odd
  if power % 2:
    childAnswer = (childAnswer * base) % modulo

  return childAnswer


def repeatedMultiplicationModulo( base, power, modulo ):

  result = 1

  for i in range(power):
    result *= base
    result %= modulo

  return result