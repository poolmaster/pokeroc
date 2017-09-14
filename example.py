#!/usr/bin/env python2.7
from __future__ import division
from datetime import date
from deck import Card
import utils

print "hello, world!\n"

print str(date.today())

C1 = Card.fromStr("hA")
C_list = utils.getCardList("hA, sk")

if C1 not in C_list:
    print "not in list"

a, b = [2, 3]
print a             
print b

print a * 1.3

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
