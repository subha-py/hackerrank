#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter = Counter(ar)
    num_pairs = 0
    for key,value in counter.most_common():
        temp=int(value/2)
        num_pairs+=temp
    return num_pairs

if __name__ == '__main__':
    result = sockMerchant(9,[10,20,20,10 ,10,30,50,10,20])
    print(result)