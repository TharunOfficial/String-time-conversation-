#

import math
import os
import random
import re
import sys


def timeConversion(s):
    lst=[]
    lst1=[]
    sum=0
    for i in range(8):
        if i!=2 and i!=5:
            lst.append(int(s[i]))
        else:
            lst.append(s[i])
    sum=int(s[0])+int(s[1])+12
    if sum>24:
        sum-=24
    lst1.append(str(sum).rstrip())
    for i in range(1):
        print(lst1[i],end='')
    for i in range(2,8):
        print(lst[i],end='')


if __name__ == '__main__':

    s = list(input().rstrip())

    result = timeConversion(s)

