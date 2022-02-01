import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
d = [0] * (N+1)

def fibo(N):
  if N == 1 or N == 2:
    return 1
  if d[N] != 0:
    return d[N]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[N] = fibo(N - 1) + fibo(N - 2)
  #return fibo(N-1) + fibo(N-2)
  return d[N]

print(fibo(N))
