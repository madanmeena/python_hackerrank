#https://www.hackerrank.com/challenges/no-idea/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
total_Element = list(input().split())
A = set(input().split())
B = set(input().split())
happiness_score=0
for x in total_Element:
    if x in A:
        happiness_score=happiness_score+1
    elif x in B:
        happiness_score = happiness_score-1

print(happiness_score)
