# https://www.hackerrank.com/challenges/strong-password/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

# Its length is at least .
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+


# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    count = 0
    
    if not re.search("[0-9]", password):
        count += 1
    if not re.search("[a-z]", password):
        count += 1
    if not re.search("[A-Z]", password):
        count += 1
    
    if not re.search("[!@#$%^&*()+-]", password):
        count += 1
        
    
    return max(count,6-n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
