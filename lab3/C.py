import sys
import bisect

def count_indices(A, L1, R1, L2, R2):
    left1 = bisect.bisect_left(A, L1)
    right1 = bisect.bisect_right(A, R1)
    
    left2 = bisect.bisect_left(A, L2)
    right2 = bisect.bisect_right(A, R2)
    
    return len(set(range(left1, right1)) | set(range(left2, right2)))

def main():

    n, q = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()  

    results = []
    for _ in range(q):
        L1, R1, L2, R2 = map(int, sys.stdin.readline().split())
        results.append(str(count_indices(A, L1, R1, L2, R2)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
