import bisect

def find_balanced_char(letters, target):
    index = bisect.bisect_right(letters, target)
    
    return letters[index] if index < len(letters) else letters[0]

n = int(input())
letters = input().split()
target = input().strip()

print(find_balanced_char(letters, target))
