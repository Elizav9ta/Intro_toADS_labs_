n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

merged = sorted(a + b)  # Merge and sort the two arrays
print(" ".join(map(str, merged)))
