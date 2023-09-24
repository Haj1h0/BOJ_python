def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    w = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    t = 0
    for i in range(1, a):
        t += m[i-1]
    t += b    
    return w[(t % 7) -1]
