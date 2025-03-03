# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

q = int(input())
for _ in range(q):
    input()
    n,k = map(int,input().split())
    INF = 10**9 * 10
    arr = [INF] * n
    ind = list(map(int,input().split()))
    val = list(map(int,input().split()))
    for i in range(k):
        arr[ind[i]-1] = val[i]
    for i in range(1,n):
        arr[i] = min(arr[i],arr[i-1]+1)
    for i in range(n-2,-1,-1):
        arr[i] = min(arr[i],arr[i+1]+1)
    
        
    print(*arr)
    