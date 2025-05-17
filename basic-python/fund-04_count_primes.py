# 🧮 Q9: Count Primes Up to N

# Write a function that returns the number of prime numbers less than or equal to n.

def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    
    # Check for divisors from 2 to num//2
    for i in range(2, num//2 + 1):
        if num % i == 0:  # If any number divides evenly, not prime
            return False
    
    # If no divisors found, it's prime
    return True

def count_primes(n):
    count = 0
    # Check each number from 2 to n
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

n = int(input())
result = count_primes(n)
print(f"Number of primes less than or equal to {n}: {result}")
