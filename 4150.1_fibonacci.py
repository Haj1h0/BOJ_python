import sys 
input = sys.stdin.readline

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현 (top-down 다이나믹 프로그래밍)

# 최대 재귀 깊이 변경을 위한 코드, 해당 코드 없을 시 Recursion Error 발생
# 재귀 깊이가 너무 깊을 시 반복문을 활용한 bottom-up 다이나믹 프로그래밍으로 대체 사용 가능
sys.setrecursionlimit(10**6)

n = int(input())

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화, index 1부터 사용
d = [0] * (n+1)

def fibo(n):
  # 종료 조건(1 혹은 2일 때 1을 반환)
  if n == 1 or n == 2:
    return 1
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[n] != 0:
    return d[n]
  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[n] = fibo(n - 1) + fibo(n - 2)
  return d[n]

print(fibo(n))
