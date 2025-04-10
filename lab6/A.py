def custom_sort(n, s):
    vowels = sorted([ch for ch in s if ch in "aeiou"])
    consonants = sorted([ch for ch in s if ch not in "aeiou"])
    print("".join(vowels + consonants))

n = int(input())
s = input().strip()

custom_sort(n, s)
