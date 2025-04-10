def find_closest_pairs(n, points):
    points.sort()  
    
    min_diff = float("inf")
    result = []
    
    # Find the minimum difference and store pairs
    for i in range(n - 1):
        diff = abs(points[i] - points[i + 1])
        if diff < min_diff:
            min_diff = diff
            result = [(points[i], points[i + 1])]
        elif diff == min_diff:
            result.append((points[i], points[i + 1]))
    
    for pair in result:
        print(pair[0], pair[1], end=" ")

n = int(input())
points = list(map(int, input().split()))

find_closest_pairs(n, points)
