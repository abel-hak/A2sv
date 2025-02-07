# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D


import sys

def max_diagonal_sum(n, m, arr):
    
    main_diag = {}  
    anti_diag = {}
    
    for i in range(n):
        for j in range(m):
            key_main = i - j  
            key_anti = i + j  

            if key_main not in main_diag:
                main_diag[key_main] = 0
            if key_anti not in anti_diag:
                anti_diag[key_anti] = 0

            main_diag[key_main] += arr[i][j]
            anti_diag[key_anti] += arr[i][j]

    

    
    max1 = 0
    for i in range(n):
        for j in range(m):
            total = main_diag[i - j] + anti_diag[i + j] - arr[i][j]  
            max1 = max(max1, total)

    return max1

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    print(max_diagonal_sum(n, m, arr))
