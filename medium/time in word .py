#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    i=" o' clock"
    f=" past "
    g=" to "
    l=" minutes"
    i1=" minute"
    h1=str(h)
    t=60-m
    m1=str(60-m)
    x=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    y=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fiveteen',               'sixteen','seventeen','eighteen','nineteen','twenty','twenty one',
        'twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine']
    if (m==0):
        return(x[h-1]+i)
    elif(m==1):
        return(y[m-1]+i1+f+x[h-1])
    elif(m==15):
        return("quarter past "+x[h-1])
    elif(m==30):
        return("half past "+x[h-1])
    elif(m==45):
        return("quarter to "+x[h])
    elif(m<30):
        return(y[m-1]+l+f+x[h-1])
    elif(m>30 and m<=59):
        return(y[t-1]+l+g+x[h])

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
