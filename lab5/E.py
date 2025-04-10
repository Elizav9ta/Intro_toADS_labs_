import heapq
import sys

def kth_largest_sum(n, k, commands):
    min_heap = []  
    total_sum = 0  
    results = []

    for cmd in commands:
        if cmd[0] == "print":
            results.append(str(total_sum))  
        else: 
            x = int(cmd[1])
            if len(min_heap) < k:
                heapq.heappush(min_heap, x)
                total_sum += x
            elif x > min_heap[0]:  
                total_sum += x - min_heap[0]
                heapq.heappushpop(min_heap, x)

    sys.stdout.write("\n".join(results) + "\n")  

n, k = map(int, input().split())
commands = [input().split() for _ in range(n)]

kth_largest_sum(n, k, commands)
