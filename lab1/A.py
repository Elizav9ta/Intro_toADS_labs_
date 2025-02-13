from collections import deque

def royal_flush(n):
    # Start with an empty deque to construct the initial deck order
    result = deque()
    
    # Reverse simulation from n to 1
    for i in range(n, 0, -1):
        # Add the card i to the front
        result.appendleft(i)
        # Rotate to mimic reversing "put at the back" steps
        if len(result) > 1:
            result.rotate(-1)
    return list(result)

# Input and output handling
t = int(input())
for _ in range(t):
    n = int(input())
    print(*royal_flush(n))
