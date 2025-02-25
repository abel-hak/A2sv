# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A


n, s = map(int, input().split())
arr = list(map(int, input().split()))  



left = 0
current_sum = 0
min_length = float('-inf')

for right in range(n):
    current_sum += arr[right]

    while current_sum > s:
        current_sum -= arr[left]
        left += 1
    min_length = max(min_length,right - left + 1)
    

if min_length != float('inf'):
    print(min_length)
    
else:
    print(-1)






    