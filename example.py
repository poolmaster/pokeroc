#!/usr/bin/env python2.7
from __future__ import division

print "hello, world!\n"

def testList(A, B):
    print B

def reorderList(A):
    B = []
    B.insert(0, A[2])
    B.insert(0, A[2])
    B.insert(0, A[2])
    for i in xrange(len(B)): 
        A[i] = B[i]

def swapElement(A):
    A[0], A[2] = A[2], A[0]
    print A

A = [1, 2, 3]
B = [4, 5, 6]
C = [4, 5, 6]

#testList(A, B)
reorderList(A)
#swapElement(A)

D = A == B
E = B == C
print D
print E
print 1/3
