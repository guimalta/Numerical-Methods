# Guilherme Malta 

import numpy as np
import matplotlib.pyplot as plt
import sys, time, datetime, os, math

from numpy import dot

def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper




def gaussElimin(a,b,digits):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = truncate(a [i,k]/a[k,k], digits)
                a[i,k+1:n] = truncate(a[i,k+1:n] - lam*a[k,k+1:n] , digits)
                b[i] = truncate( b[i] - lam*b[k] , digits)
    for k in range(n-1,-1,-1):
        b[k] = truncate((b[k] - dot(a[k,k+1:n],b[k+1:n]))/a[k,k] , digits)
    return b


