import math
import numpy as np

p = np.pi
print (math.pow(10, 2))

print (10. ** 2)

def p2(n):
    return pow(n,2)
def MakeR(R,r,rr):
    return R+r+rr
def LformT(C,T,R,Yobun=0):
    x2 = 16*p2(p)/p2(T)
    x1 = (-4)*(1/C) + Yobun
    x0 = p2(R)
    si = np.poly1d([x2,x1,x0])
    return si.r
def BformT(Q,QT,C,T,R):
    d = -np.log(QT/Q)/R
    d*= 2
    return LformT(C,T,R,d)

time = LformT(1,2,3)
print(time)