# Problem: Books - https://codeforces.com/contest/279/problem/B

n , t = (map(int,input().split()))

arr = list(map(int,input().split()))
sum = 0
left = 0
max1 = float('-inf')
for right in range(n):
    sum += arr[right]
    
    while sum > t and left <= right:
        sum -= arr[left]
        left += 1
    max1 = max(max1,right - left + 1)
print(max1)
    
        
