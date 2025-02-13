def sieve_of_eratosthenes(limit: int) -> list:
    """Generates primes up to the given limit."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return primes

def find_nth_superprime(n: int) -> int:
    # Estimate: we need at least 1000 primes for safety
    primes = sieve_of_eratosthenes(10000)
    # Get the first `n` prime indices
    superprimes = [primes[i - 1] for i in primes[:n]]
    return superprimes[n - 1]

# Input
n = int(input())
print(find_nth_superprime(n))
