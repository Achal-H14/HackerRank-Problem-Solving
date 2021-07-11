# https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if(s[8:]=='AM'  ):
        if s[:2]=='12' :
            time="00"+s[2:-2]
        else:
            time=s[:-2]
        
   
        
    elif(s[8:]=='PM' ):
        if s[:2]=='12':
            time=s[:-2]
        else:
         
            time=str(int(s[:2])+12)+s[2:-2]
    
    return time;

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
