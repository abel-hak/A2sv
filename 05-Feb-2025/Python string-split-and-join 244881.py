# Problem: Python string-split-and-join - https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true



def split_and_join(line):
    result = line.split(" ")
    return "-".join(result)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)