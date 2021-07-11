# https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    nn=0
    np=0
    n0=0
    l=len(arr)
    
    for i in arr:
     
        if i<0:
            nn +=1
        elif i>0:
            np += 1 
        else:
            n0 += 1
            
    print(np/l)
    print(nn/l)
    print(n0/l)
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
