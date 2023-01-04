# Define function to test for primality
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

# Define function to find prime values in a range
def find_primes(start, end):
  primes = []
  for i in range(start, end+1):
    if is_prime(i):
      primes.append(i)
  return primes

# Test function
primes = find_primes(2, 999)
print("Number of primes:", len(primes))
print("Sum of primes:", sum(primes))
