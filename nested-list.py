#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name,score))
    lowestScore=min(students,key=lambda x:x[1])
    secondlist=list(filter(lambda x: float(x[1]) > lowestScore[1], students))
    secondlowestScore=min(secondlist,key=lambda x:x[1])
    #print(secondlowestScore)
    finallist = list(filter(lambda x: x[1] == secondlowestScore[1], secondlist))
    
    finallist.sort(key=lambda x:x[0])
    for x in finallist:
        print(x[0])
