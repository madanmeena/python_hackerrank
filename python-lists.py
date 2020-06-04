#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    operations = []
    for _ in range(N):
        name = input()   
        #print(name)             
        if 'insert' in name:
            ops = name.split(" ")
            #print(ops)
            operations.insert(int(ops[1]),int(ops[2]))
            #print(operations)
        elif 'print' in name:
            print(operations)
        elif 'remove' in name:
            ops = name.split(" ")
            #print(ops)
            operations.remove(int(ops[1]))
            #print(operations)
        elif 'append' in name:
            ops = name.split(" ")
            #print(ops)
            operations.append(int(ops[1]))
            #print(operations)
        elif 'sort' in name:
            operations.sort()
            #print(operations)
        elif 'pop' in name:
            operations.pop()
            #print(operations)
        elif 'reverse' in name:
            operations = list(reversed(operations))
            #print(operations)