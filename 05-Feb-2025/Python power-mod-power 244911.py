# Problem: Python power-mod-power - https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input values
a = int(input().strip())
b = int(input().strip())
m = int(input().strip())

# Print a^b
print(pow(a, b))

# Print (a^b) % m
print(pow(a, b, m))
