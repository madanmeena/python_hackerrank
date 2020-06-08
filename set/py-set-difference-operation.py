#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
first_integer_list = map(int, input().split())
m = int(input())
second_integer_list = map(int, input().split())
first_set=set(first_integer_list)
second_set=set(second_integer_list)
total_element = first_set.difference(second_set)
print(len(total_element))