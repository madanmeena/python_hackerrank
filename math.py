#https://www.hackerrank.com/challenges/polar-coordinates/problem
from cmath import phase
number = complex(input())
print(abs(number))
print(phase(number))
#https://www.hackerrank.com/challenges/find-angle/problem
import math
AB = int(input())
BC = int(input())

print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')

#https://www.hackerrank.com/challenges/python-mod-divmod/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
number = divmod(int(input()),int(input()))
print(number[0])
print(number[1])
print(number)