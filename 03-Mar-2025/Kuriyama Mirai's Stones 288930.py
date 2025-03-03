# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
arr = list(map(int,input().split()))
pre_arr = [0] * (n + 1)
sum1 = 0
for i in range(n):
    sum1 += arr[i]
    pre_arr[i+1] = sum1
 
    
temp = sorted(arr)
pre_tem = [0] * (n + 1)
sum2 = 0
for i in range(n):
    sum2 += temp[i]
    pre_tem[i+1] = sum2
    
t = int(input())
for _ in range(t):
    k,l,r = map(int,input().split())
    sum = 0
    if k == 1:
        sum = pre_arr[r] - pre_arr[l-1]
    else:
        sum = pre_tem[r] - pre_tem[l-1]
        
    print(sum)