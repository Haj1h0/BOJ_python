n = int(input())

# 맨 마지막 층의 최대값 정보 담는 리스트
dp = [0 for i in range(n)]

for _ in range(n):
  # 삼각형의 맨 꼭대기 층부터 값 하나씩 입력 받기
  floor = list(map(int,input().split()))
  for i in range(len(floor)):
    if i >= 1: 
      floor[i] = max(dp[i-1],dp[i]) + floor[i]
    else:  # index 0인 경우
      floor[i] += dp[i] 

  # 다음 층 계산을 위해 해당 층마다 floor list에 최대 경로 구한 값을 dp리스트로 옮기기  
  dp[:len(floor)] = floor[:len(floor)]  

print(max(dp))
