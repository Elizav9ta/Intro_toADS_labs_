import sys
import bisect

def solve():

    N = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    X = int(sys.stdin.readline().strip())

    pos = bisect.bisect_left(arr, X)

    if pos < N and arr[pos] == X:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()
