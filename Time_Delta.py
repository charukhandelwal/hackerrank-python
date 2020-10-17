#!/bin/python

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
     a=datetime.datetime.strptime(t1,'%a %d %b %Y %H:%H:%S %z')
     b=datetime.datetime.strptime(t2,'%a %d %b %Y %H:%H:%S %z')
     return str(int(abs(a-b).total))
if __name__ == '__main__':
    
    t = int(input().strip())

    for t_itr in xrange(t):
        t1 = raw_input()

        t2 = raw_input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
