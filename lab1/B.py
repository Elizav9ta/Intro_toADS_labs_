def find_closest_younger(n, ages):
    result = []
    stack = []  # Stores (index, age) pairs
    
    for i in range(n):
        # Remove elements from stack that are not younger
        while stack and stack[-1][1] >= ages[i]:
            stack.pop()
        
        # Append the closest younger person's age or -1 if none found
        result.append(stack[-1][1] if stack else -1)
        
        # Push current person onto the stack
        stack.append((i, ages[i]))
    
    print(" ".join(map(str, result)))


# Input reading
n = int(input().strip())
ages = list(map(int, input().strip().split()))

# Function call
find_closest_younger(n, ages)
