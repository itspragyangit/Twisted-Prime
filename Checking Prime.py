  
def isprime(num):
  # prime number ---> 2 factors
  faclst= [ ]
  a = num+1
  for i in range(1,a):
    if (num % i == 0):
      faclst.append(i)
  len_faclst = len(faclst)
  if len_faclst == 2:
    return True
  else:
    return False
isprime(56)
