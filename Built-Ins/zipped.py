#https://www.hackerrank.com/challenges/zipped/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
firstline = input().split()
totalStudent = int(firstline[0])
numberofline = int(firstline[1])
totalMarks=[]
for i in range(numberofline):
    totalMarks=totalMarks+[list(map(float,input().split()))]

marksZipped = list(zip(*totalMarks))
for i in range(totalStudent):
    student = marksZipped[i]
    print("{:.2f}".format(sum(student)/len(student)))