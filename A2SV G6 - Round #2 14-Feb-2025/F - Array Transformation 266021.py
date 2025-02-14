# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

n = int(input())
for _ in range(n):
    t = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for i in range(t):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1

    res = list(d.values())
    res.sort()
    m = len(res)
    min1 = float('inf')
    for i in range(m):
        ke = t - (res[i]*(m-i))
        min1 = min(min1,ke)
    print(min1)
        
    
    
    