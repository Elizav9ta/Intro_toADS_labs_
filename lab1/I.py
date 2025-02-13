from collections import deque

def find_leader(n: int, students: str) -> str:
    s_queue = deque()
    k_queue = deque()
    
    for i in range(n):
        if students[i] == 'S':
            s_queue.append(i)
        else:
            k_queue.append(i)
    
    while s_queue and k_queue:
        s_idx = s_queue.popleft()
        k_idx = k_queue.popleft()
        
        if s_idx < k_idx:
            s_queue.append(s_idx + n)
        else:
            k_queue.append(k_idx + n)
    
    return "SAKAYANAGI" if s_queue else "KATSURAGI"

n = int(input())
students = input().strip()
print(find_leader(n, students))
