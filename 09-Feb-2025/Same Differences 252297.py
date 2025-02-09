# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = {}
    cou = 0
    for i in range(n):
        key = arr[i] - i
        if key in freq:
                
            cou += freq[key]
        freq[key] = freq.get(key,0) + 1
                
        
        
    print(cou)