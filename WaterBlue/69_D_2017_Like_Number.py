def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """100
"""
input = get_input(INPUT)
#######
import math
N = 100001
pr = [True]*(N+1)
pr[0] = pr[1] = False
for i in range(2,int(math.sqrt(N))+1) :
    if pr[i]:
        print(i)
        for j in range(i+i,N,i):pr[j] = False

c = [0]*(N+1)

for i in range(3,N,2):
    if pr[i] and pr[(i+1)//2]:
        c[i]+=1
for i in range(3,N):
    c[i]+=c[i-1]
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(c[r]-c[l-1])
