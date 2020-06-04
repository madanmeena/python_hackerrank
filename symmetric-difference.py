#https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
first_integer_list = map(int, input().split())
m = int(input())
second_integer_list = map(int, input().split())
first_set=set(first_integer_list)
second_set=set(second_integer_list)
common_element = first_set.intersection(second_set)
total_element = first_set.union(second_set)
unique_elment = total_element.difference(common_element)
unique_elment_list = list(unique_elment)
for x in sorted(unique_elment):
    print(str(x))