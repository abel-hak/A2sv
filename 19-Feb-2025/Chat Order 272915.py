# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
arr = []
for _ in range(n):
    name = input()
    arr.append(name)
arr = arr[::-1]
seen = set()
for i in arr:
    if i not in seen:
        seen.add(i)
        print(i)

    
    
    