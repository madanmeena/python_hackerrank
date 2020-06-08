#https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
int(input())
first_integer_list = map(int, input().split())
first_set=set(first_integer_list)
operations = []
N = int(input())
for i in range(N):
    name= input()   
    second_set = set(map(int, input().split()))
    
    if 'intersection_update' in name:           
        first_set.intersection_update(second_set)
    elif 'difference_update' in name:        
        first_set.difference_update(second_set)
    elif 'symmetric_difference_update' in name:     
        first_set.symmetric_difference_update(second_set)
    elif 'update' in name:
        first_set.update(second_set)

print(sum(first_set))
