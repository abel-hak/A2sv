# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n , k = map(int,input().split())

arr = list(map(int,input().split()))

left = 0
max1 = float('-inf')
dicc = defaultdict(int)
res = []

for right in range(n):
    dicc[arr[right]] += 1

    while len(dicc) > k and left <= right:
       
        if dicc[arr[left]] < 2:
            del dicc[arr[left]]
        else:
            dicc[arr[left]] -= 1

        left += 1
    if right - left + 1 > max1:
        max1 = right - left + 1
        res = [left+1,right+1]
    
print(*res)