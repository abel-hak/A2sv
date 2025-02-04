# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n = int(input())

for i in range(n):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        ss = s[1:len(s) - 1]
        print(s[0] + str(len(ss)) + s[-1])
