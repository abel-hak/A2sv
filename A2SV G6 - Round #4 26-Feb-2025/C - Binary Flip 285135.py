# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

import sys

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    left = -1
    ones, zeros = 0, 0
    diff = 0
    flag = True
    check = False
    

    for right in range(n):
        if a[right] == '1':
            ones += 1
        else:
            zeros += 1
        
        
        if a[right] != b[right]:
            diff += 1
        if ones == zeros:
            if diff != 0 and diff != right - left:
                flag = False
                break
            diff = 0
            left = right
       
    if (diff != 0 and diff != n - left):
        flag = False

    print("YES" if flag else "NO")
