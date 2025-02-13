def nth_prime(n: int) -> int:
    upper_bound = 10000  
    sieve = [True] * (upper_bound + 1)
    sieve[0], sieve[1] = False, False
    
    primes = []
    
    for p in range(2, upper_bound + 1):
        if sieve[p]:
            primes.append(p)
            for multiple in range(p * p, upper_bound + 1, p):
                sieve[multiple] = False
        if len(primes) >= n:
            break
    
    return primes[n - 1]

n = int(input())
print(nth_prime(n))
