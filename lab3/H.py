import sys
import bisect

def solve():
    N, M = map(int, sys.stdin.readline().split())
    
    blocks = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * N
    prefix[0] = blocks[0]
    
    for i in range(1, N):
        prefix[i] = prefix[i - 1] + blocks[i]
    
    results = []
    for _ in range(M):
        line = int(sys.stdin.readline().strip())
        block_idx = bisect.bisect_left(prefix, line) + 1  
        results.append(str(block_idx))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
