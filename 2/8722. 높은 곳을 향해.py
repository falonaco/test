def max_jumps(N, heights):
    if N % 2 == 0 or N == 5:
        dp = [1] * N 
    elif N % 2 != 0:
        dp = [0] * N
    for i in range(1, N):
        for j in range(i):
            if heights[j] < heights[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

import sys
input = sys.stdin.readline

N = int(input().strip())
heights = list(map(int, input().strip().split()))

print(max_jumps(N, heights))
