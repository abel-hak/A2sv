# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

from collections import defaultdict

def minion_game(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    stuart_score = 0  
    kevin_score = 0   

    for i in range(len(string)):
        if string[i].lower() in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif stuart_score < kevin_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
