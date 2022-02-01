import sys 
input = sys.stdin.readline

# 피보나치 함수(Fibonacci Function)를 반복문으로 구현 (bottom-up 다이나믹 프로그래밍)

n = int(input())

# dp table index 1 start, N 받는 사이즈에 따라 dp list 생성 시, n = 1인 경우 index Error
if n < 3:
  dp = [0] * 3
else:
  dp = [0] * (n+1)

# dp table은 index 1부터 사용해야 for문에서 다루기 편하다.
dp[1] = 1
dp[2] = 1    

# n < 3 인 경우 for문 자체에 들어가지 못한다.
for i in range(3,n+1):  
  dp[i] = (dp[i-1] + dp[i-2]) 
  
print(dp[n])
