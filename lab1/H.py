import math

def is_prime(n: int) -> str:
    if n <= 1:
        return "NO"
    if n <= 3:
        return "YES"
    if n % 2 == 0 or n % 3 == 0:
        return "NO"
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "NO"
    return "YES"

# Input
n = int(input())
print(is_prime(n))
