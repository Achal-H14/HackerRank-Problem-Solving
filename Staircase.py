# https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    
    for i in range(n):
        for j in range(n):
            if j>=n-1-i:
                print("#",end='')
            else:
                print(" ",end='')
        print()
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
