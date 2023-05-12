# Faster Prime Finding
# Write a function that returns a list of all primes up to a given number.

# For each number, in order to determine if it is prime, take the following steps:

# Find the square root of the number
# Find all the primes up to that square root
# Test to see if any of those primes are divisors
# If a number has no prime divisors, it is prime!

def isPrime(num):
    if num % 2 == 0: # even numbers
        return False
    for factor in range(3, int(num ** 0.5) + 1, 2):
        if num % factor == 0: # odd numbers only, but not prime
            return False
    return True

def allPrimesUpTo(num):
    primes = [2]
    for factor in range(3, num + 1):
        if isPrime(factor):
            primes.append(factor)
    return primes


print(allPrimesUpTo(100))