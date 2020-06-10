#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
cube = lambda x: x*x*x # complete the lambda function 

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fibonacci(n):
    # return a list of fibonacci numbers
    fibseries= list()
    for x in range(1,n+1):
        fibseries.append(fib(x))
    return fibseries

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#https://www.hackerrank.com/challenges/reduce-function/problem
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y:Fraction(x.numerator*y.numerator,x.denominator*y.denominator),fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)