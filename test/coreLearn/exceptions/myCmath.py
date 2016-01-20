#!/usr/bin/env python
# coding:utf8

from math import *

oldSqrt = sqrt
del sqrt


def sqrt(num):
    try:
        return oldSqrt(num)
    except (TypeError, ValueError), e:
        return None

if __name__ == '__main__':
    print sqrt(23)
