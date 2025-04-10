n = int(input())  
for _ in range(n):
    words = input().split()
    words.sort(key=len)  
    print(" ".join(words))
