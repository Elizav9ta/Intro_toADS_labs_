def check_password(password: str, k: int, text: str) -> str:
    return "YES" if text.count(password) >= k else "NO"

# Reading input
P, k = input().split()
k = int(k)
T = input().strip()

# Output the result
print(check_password(P, k, T))
