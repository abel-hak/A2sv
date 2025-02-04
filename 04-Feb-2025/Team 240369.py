# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())
co = 0
for i in range(n):
    arr = list(map(int, input().split()))
    cou1 = 0
    cou2 = 0
    for a in arr:
        if a == 1:
            cou1 += 1
        else:
            cou2 += 1
    if cou1 > cou2:
        co += 1
print(co)
    