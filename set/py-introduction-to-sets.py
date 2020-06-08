#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
    distinct = set(array)
    return sum(distinct)/len(distinct)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)