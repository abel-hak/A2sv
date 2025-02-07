# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s , n = map(int,input().split())
y = []
x = []
for _ in range(n):
    xx , yy = map(int,input().split())
    y.append(yy)
    x.append(xx)
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            x[i],x[j] = x[j],x[i]
            y[i],y[j] = y[j],y[i]
        elif x[i] == x[j]:
            if y[i] > y[j]:
                x[i],x[j] = x[j],x[i]
                y[i],y[j] = y[j],y[i]

cou = 0              
for i in range(len(x)):
    if s > x[i]:
        s += y[i]
        cou += 1
    else:
        print("NO")
        break
if cou == len(x):
    print("YES")