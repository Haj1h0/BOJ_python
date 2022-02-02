n = int(input())
tri = [[0]*n for _ in range(n)]

for i in range(n):
  floor = list(map(int,input().split()))
  tri[i][:i+1] = floor

for flr in range(n):  
  if flr > 0:   # 2층 이상일 때만 연산 동작
    for i in range(flr+1):  # 전 층의 값을 통해 현재 층의 값 maximum으로 최신화
      if i == 0:  # index 0
        tri[flr][0] += tri[flr-1][0]
      else:
        tri[flr][i] += max(tri[flr-1][i-1],tri[flr-1][i])
  
print(max(tri[n-1]))
      
# 1932.2py와 다르게 추가적인 dp table 구현없이 초기 tri list안에서 최신화
