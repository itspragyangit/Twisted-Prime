def isTwistedPrime(n):
  if isprime(n):
    rev_n = reverse_int(n)
    if isprime(rev_n):
      return True
  return False
isTwistedPrime(79)
