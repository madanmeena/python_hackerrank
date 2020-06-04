#https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
stamps = set()
for _ in range(int(input())):
    stamps.add(input())
print(len(stamps))