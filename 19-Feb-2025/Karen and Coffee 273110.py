# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import defaultdict
arr = list(map(int,input().split()))
max1 = 200000
n,k,q = arr[0],arr[1],arr[2]
freq = [0] * (max1 + 2)
for _ in range(n):
    l,r = map(int,input().split())
    
    freq[l] += 1
    freq[r+1] -= 1

cum_sum = freq[0]
for i in range(1,max1+1):
    cum_sum += freq[i]
    freq[i] = cum_sum
admiss = [0] * (max1 + 1)



for i in range(1,max1+1):
    admiss[i] = 1 if freq[i] >= k else 0

prefix = [0] * (max1 + 1)
for i in range(1,max1+1):
    prefix[i] = prefix[i-1] + admiss[i]

for _ in range(q):
    a,b = map(int,input().split())
    print(prefix[b] - prefix[a-1] )

    

