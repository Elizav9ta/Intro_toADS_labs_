from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split())) if n > 0 else []
b = list(map(int, input().split())) if m > 0 else []

count_a = Counter(a)
count_b = Counter(b)

common = []
for num in count_a:
    if num in count_b:
        common.extend([num] * min(count_a[num], count_b[num]))

print(" ".join(map(str, sorted(common))))
