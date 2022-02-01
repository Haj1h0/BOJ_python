N = int(input())

house = []  # i줄의 R,N,B cost, 2차원 리스트

for _ in range(N):
  house.append(list(map(int,input().split())))

house.reverse() # house.reverse() 자체는 none, 객체 존재 x

for i, lst in enumerate(house):
  if i > 0: # house[0]의 리스트에서는 연산이 필요 없다.
    lst[0] += min(house[i-1][1],house[i-1][2])
    lst[1] += min(house[i-1][0],house[i-1][2])
    lst[2] += min(house[i-1][0],house[i-1][1])
  # house 리스트 자체에서 min값 최신화 하면서 올라간다.  
  """
  print(house)
  [[13, 89, 99], [49, 60, 57], [26, 40, 83]]
  [[13, 89, 99], [138, 73, 70], [26, 40, 83]]
  [[13, 89, 99], [138, 73, 70], [96, 110, 156]]
  """

print(min(house[N-1]))
