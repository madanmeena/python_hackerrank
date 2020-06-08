#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    stringDict={}
    for x in s:
        if x in stringDict:
            stringDict[x]=stringDict[x]+1
        else:
            stringDict[x]=1
    
    print(stringDict)
    minfrequency=len(s)
    maxfrequency=1
    maxOccurence=0
    minOccurence=0
    for key, x in stringDict.items():
        if minfrequency>=x:
            if minfrequency==x:
                minOccurence = minOccurence+1
            else:
                minfrequency=x
                minOccurence = 1
        if maxfrequency<=x:
            if maxfrequency==x:
                maxOccurence=maxOccurence+1
            else:
                maxfrequency=x
                maxOccurence=1
    print(minfrequency)      
    print(maxfrequency)
    print(maxOccurence)
    print(minOccurence)
    if (maxfrequency==minfrequency or maxfrequency==minfrequency+1) and (maxOccurence==1 or minOccurence==1):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()