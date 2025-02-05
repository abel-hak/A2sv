# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter

def can_transform(s, t, p):
    
    i = 0  
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
 
    if i != len(s):
        return "NO"
    

    count_s = Counter(s)
    count_t = Counter(t)
    count_p = Counter(p)
    
   
    for char in count_t:
        needed = count_t[char] - count_s.get(char, 0)
        if needed > 0:
            if count_p.get(char, 0) < needed:
                return "NO"
    
    return "YES"


q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    print(can_transform(s, t, p))
