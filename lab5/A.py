import heapq

def min_merge_cost(n, sizes):
    heapq.heapify(sizes)  
    total_cost = 0

    while len(sizes) > 1:
        a = heapq.heappop(sizes) 
        b = heapq.heappop(sizes)  
        cost = a + b
        total_cost += cost
        heapq.heappush(sizes, cost)  

    return total_cost

n = int(input())
sizes = list(map(int, input().split()))

print(min_merge_cost(n, sizes))
