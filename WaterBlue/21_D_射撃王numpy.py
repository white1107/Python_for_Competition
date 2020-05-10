def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
5 6
12 4
14 7
21 2
"""
input = get_input(INPUT)
#######

import numpy as np
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
print(zip(*A))
print(A)
B,C=zip(*A)
B=np.array(B)
C=np.array(C)
t=np.arange(N)
print(t)
def f(x):
  D=(x-B)/C
  D.sort()
  return (D>=t).all()
ng=0
ok=10**18
while ok-ng>1:
  mid=(ok+ng)//2
  if f(mid):
    ok=mid
  else:
    ng=mid
print(ok) 