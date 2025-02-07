# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    arr = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
    arr.sort(key= lambda x:(x[1],x[0]))
    min1 = arr[0][1]
    min2 = 0
    for s in arr:
        if s[1] > min1:
            min2 = s[1]
            break
    res = []
    for i in arr:
        if i[1] == min2:
            print(i[0])
    
            
    

    
    
        
        
    
        
