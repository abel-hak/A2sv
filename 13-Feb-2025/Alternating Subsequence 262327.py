# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n == 1:
        print(arr[0])
        continue

    total_sum = 0
    max_element = arr[0]

    for i in range(1, n):
        if (arr[i] > 0 and arr[i - 1] < 0) or (arr[i] < 0 and arr[i - 1] > 0):
            total_sum += max_element
            max_element = arr[i]
        else:
            max_element = max(max_element, arr[i])
    
    total_sum += max_element
    print(total_sum)
