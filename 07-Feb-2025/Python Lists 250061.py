# Problem: Python Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    
    lst = []  

    for _ in range(N):
        command = input().split()  
        cmd = command[0]

        if cmd == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(int(command[1]))
        elif cmd == "append":
            lst.append(int(command[1]))
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
