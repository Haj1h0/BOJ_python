import sys 
input = sys.stdin.readline

N = int(input())
# dp list index 1 start, N 받는 사이즈에 따라 dp list 생성 시, N = 1인 경우 index Error
# dp = [0] * 1000001
dp = [0 for i in range(1000002)]

# dp list는 가급적 index 1부터 사용해야 for문에서 다루기 편하다.
dp[1] = 1
dp[2] = 2

# bottom-up
# N < 3 인 경우 for문 자체에 들어가지 못한다.
for i in range(3,N+1):  
  # 각 연산마다 %를 해주지 않으면 메모리 초과 발생
  dp[i] = (dp[i-1] + dp[i-2]) % 15746
  
print(dp[N])
  
