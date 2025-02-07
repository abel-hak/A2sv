# Problem: Runner up score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    seen = set()
    res = []
    for i in arr:
        if i not in seen:
            seen.add(i)
            res.append(i)
    res.sort()

    print(res[-2])
        