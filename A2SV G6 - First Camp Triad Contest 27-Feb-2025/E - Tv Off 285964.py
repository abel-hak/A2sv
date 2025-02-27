# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

import sys
input = sys.stdin.readline

def iinp(): return int(input())
def minp(): return map(int, input().split())

def solve():
    n = iinp()

    queries = []
    arr = set()
    for _ in range(n):
        l, r = minp()
        queries.append((l, r + 1))  
        arr.add(l)
        arr.add(r + 1)

    arr = sorted(arr)  
    mp = {value: index for index, value in enumerate(arr)} 
   

  
    pf = [0] * len(arr)
    for l, r in queries:
        pf[mp[l]] += 1
        pf[mp[r]] -= 1
       
  
    for i in range(1, len(arr)):
        pf[i] += pf[i - 1] 
  

   
    for i in range(len(arr)):
        if pf[i] != 1:
            pf[i] = 0

    
    pf2 = [0] * len(arr)
    for i in range(1, len(arr)):
        pf2[i] = pf[i - 1] + pf2[i - 1]

   
    for i, (l, r) in enumerate(queries):
        if pf2[mp[r]] - pf2[mp[l]] == 0:
            print(i + 1)
            return
    print(-1)

def main():
    t = 1  
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
