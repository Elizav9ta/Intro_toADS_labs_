def min_repeats(A: str, B: str) -> int:
    repeats = 1
    extended_A = A
    
    while len(extended_A) < len(B) + len(A):
        if B in extended_A:
            return repeats
        extended_A += A
        repeats += 1
    
    return repeats if B in extended_A else -1

# Reading input
A = input().strip()
B = input().strip()

# Output the result
print(min_repeats(A, B))
