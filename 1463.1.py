import sys 
input = sys.stdin.readline

n = int(input())
dp = [0,0,1,1]    
# dp table 인덱스 1부터 시작, 정수 x를 1로 만드는데 필요한 최솟값 y, dp[x] = y

for i in range(4,n+1):
    m = 0
    if i % 3 == 0 and i % 2 == 0:
        m = min(dp[i-1] + 1, dp[i//3] + 1, dp[i//2] + 1)
    elif i % 2 == 0:
        m = min(dp[i-1] + 1, dp[i//2] + 1)
    elif i % 3 == 0:
        m = min(dp[i-1] + 1, dp[i//3] + 1)
    else:   # if i % 3 != 0 and i % 2 != 0:
        m = dp[i-1] + 1
    dp.append(m)

print(dp[n])

"""
Exception has occurred: TypeError X
list indices must be integers or slices, not float
When you do x / y, an integer is returned in Python 2.x.
However in 3.x, the '/' operator performs 'true' division, resulting in a float instead of an integer.
"""
