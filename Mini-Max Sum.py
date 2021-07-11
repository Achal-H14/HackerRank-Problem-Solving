# https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_of_arr=sum(arr)
    arr_of_sum=[]
    
    for i in range(len(arr)):
        arr_of_sum.append(sum_of_arr - arr[i])
        
    print(min(arr_of_sum), max(arr_of_sum))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
