# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=false

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    h = "hackerrank"
    
    count = 0
    if len(s) >= len(h):
        for i in range(len(s)):
            if count < len(h) and s[i] == h[count]:
                count += 1
        
        if count >= len(h):
            return "YES"
        
    return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
