#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?h_r=next-challenge&h_v=zen
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    name = input()              
    if 'pop' in name:
        s.pop()
    elif 'remove' in name:
        ops = name.split(" ")    
        s.remove(int(ops[1]))    
    elif 'discard' in name:
        ops = name.split(" ")        
        s.discard(int(ops[1]))
        
print(sum(s))