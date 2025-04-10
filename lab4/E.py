from collections import defaultdict, deque

def max_tree_width(n, edges):
    if n == 1:
        return 1  

    tree = defaultdict(lambda: [None, None])  
    for x, y, z in edges:
        tree[x][z] = y

    queue = deque([(1, 1)]) 
    level_count = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        level_count[level] += 1  

        left, right = tree[node]
        if left:
            queue.append((left, level + 1))
        if right:
            queue.append((right, level + 1))

    return max(level_count.values())  

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

print(max_tree_width(n, edges))
