def min_subarray_length(n, S, arr):
    left = 0
    curr_sum = 0
    min_length = float('inf')

    for right in range(n):
        curr_sum += arr[right]

        while curr_sum >= S:
            min_length = min(min_length, right - left + 1)
            curr_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else -1  

n, S = map(int, input().split())
arr = list(map(int, input().split()))
print(min_subarray_length(n, S, arr))
