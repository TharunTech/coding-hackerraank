
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    s1=0
    s2=0
    for i in range(0,len(arr)):
        s1+=arr[i][i]
    for f in range(0,len(arr)):
        l=0
        s2+=arr[len(arr)-f-1][f]
        l=l+1
    print(s1)
    print(s2)
    return abs(s1-s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
