def balance_bst(arr):
    """Переставляет элементы массива, чтобы при вставке получился сбалансированный BST."""
    if not arr:
        return []
    
    arr.sort()  
    mid = len(arr) // 2  
    
    return [arr[mid]] + balance_bst(arr[:mid]) + balance_bst(arr[mid+1:])

n = int(input())
arr = list(map(int, input().split()))

print(*balance_bst(arr))
