#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxScore = max(arr)
    lsitwithoutmax = list(filter(lambda x: x < maxScore, arr))
    runnerUpScore = max(lsitwithoutmax)
    print(runnerUpScore)