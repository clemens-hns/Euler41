# Euler 41

def permutations(string, step = 0, biggest_prime=0):
  bp = biggest_prime
  # if we've gotten to the end, print the permutation
  # everything to the right of step has not been swapped yet
  for i in range(step, len(string)):
    # copy the string (store as array)
    string_copy = [character for character in string]
    # swap the current index with the step
    string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
    # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
    permutations(string_copy, step + 1, bp)
  string = "".join(string)
  n = int(string)
  if(isPrime(n)):
  	if(n > bp):
	  bp = n
	  print " Prime: ", n
	
def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    
  

num_str = "12345678"
permutations(num_str)



