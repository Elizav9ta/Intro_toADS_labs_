def find_nearest_number():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    
    closest_index = 0
    min_distance = abs(nums[0] - target)
    
    for i in range(1, n):
        distance = abs(nums[i] - target)
        if distance < min_distance:
            closest_index = i
            min_distance = distance
    
    print(closest_index)


find_nearest_number()
