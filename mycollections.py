#https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
input()
myShoeSize = Counter(map(int,input().split()))
moneyEarned = 0
for cust in range(int(input())):    
    size,price = map(int,input().split())    
    if size in myShoeSize and myShoeSize[size]>0:        
        myShoeSize[size] = myShoeSize[size]-1
        moneyEarned = moneyEarned+ price
    
print(moneyEarned)

#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
acount, bcount = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for index in range(1,acount+1):
    d[str(input())].append(index)
for index in range(bcount):
    output=d[str(input())]
    if len(output)>0:
        print("{0}".format(' '.join(map(str,output))))
    else:
        print("-1")
