def is_balanced(s: str) -> str:
    stack = []
    for char in s:
        # If stack has a matching pair, pop it
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "YES" if not stack else "NO"

s = input().strip()
print(is_balanced(s))
