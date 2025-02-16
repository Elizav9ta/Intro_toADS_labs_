import sys
import math

def can_steal_all(gold, H, K):
    total_hours = sum(math.ceil(g / K) for g in gold)
    return total_hours <= H

def find_min_steal_speed(N, H, gold):
    left, right = 1, max(gold) 
    
    while left < right:
        mid = (left + right) // 2  
        if can_steal_all(gold, H, mid):
            right = mid  
        else:
            left = mid + 1  
    
    return left  

def solve():

    N, H = map(int, sys.stdin.readline().split())
    gold = list(map(int, sys.stdin.readline().split()))
    
    print(find_min_steal_speed(N, H, gold))

if __name__ == "__main__":
    solve()
