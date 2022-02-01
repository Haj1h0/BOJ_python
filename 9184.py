import sys
input = sys.stdin.readline

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화, index 1부터 사용
# cf) [[0,0]*2] = [[0,0,0,0]] 리스트 곱셈으로 동작
dp = [[[0 for i in range(21)] for i in range(21)] for i in range(21)]

# top-down
def w(a, b, c):  # -50 ≤ a,b,c ≤ 50

    # 종료 조건, 0 < a,b,c <= 20 값만 dp table에 기록 되어짐
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # dp table에 이미 계산한 적 있는 문제라면 그대로 반환
    elif dp[a][b][c] != 0:
        return dp[a][b][c]

    # 점화식    
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
  a, b, c = map(int, input().split())

  # 종료 조건
  if a == -1 and b == -1 and c == -1:
    break

  print("w(%d, %d, %d) =" %(a, b, c), w(a, b, c))
