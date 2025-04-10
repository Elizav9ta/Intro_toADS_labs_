import heapq

def max_earnings(n, m, seats):
    seats = [-s for s in seats]
    heapq.heapify(seats)

    total_earnings = 0

    for _ in range(m):
        max_seat = -heapq.heappop(seats) 
        total_earnings += max_seat
        
        if max_seat > 1:
            heapq.heappush(seats, -(max_seat - 1))  

    return total_earnings

n, m = map(int, input().split())
seats = list(map(int, input().split()))

print(max_earnings(n, m, seats))
