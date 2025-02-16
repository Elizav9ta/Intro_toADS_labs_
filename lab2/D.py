from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counter = Counter(numbers)

max_freq = max(counter.values())

modes = sorted([num for num, freq in counter.items() if freq == max_freq], reverse=True)

print(*modes)
