# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    
    trf = 0
    count = 0
    for i in arr:
        if i >= x:
            trf += i - x
            count+=1
        else:
            needd = x - i
            if trf >= needd:
                count+=1
                trf = trf - needd
            
            
            
    print(count)            