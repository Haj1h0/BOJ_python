for _ in range(int(input())):
  
  tri = [1,1,1]
  n = int(input())
  for i in range(2,n):
    tri.append(tri[i-1]+tri[i-2])
    # 점화식 : tri[i] = tri[i-3] + tri[i-2]
  print(tri[n-1])

