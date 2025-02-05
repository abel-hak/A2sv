# Problem: Swap Case - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    ss=""
    for i in s:
        if i.islower():
            ss += i.upper()
        else:
            ss += i.lower()
    return ss

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)