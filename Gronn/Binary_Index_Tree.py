def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """8
1 2 3 4 5 6 7 8
"""
input = get_input(INPUT)
#####################################

N = int(input())
A = list(map(int,input().split()))
bit = [0]*(N+1)
'''
def add(a,w):
    ret = 0
    for i in range(a,0,-(i&-i)):ret += bit[i]
    return ret
'''
def add(a,w):
    x = a
    while x<=N:
        bit[x]+=w
        x+=x&-x
def sum(a):
    ret = 0
    x = a
    while x>0:
        ret+=bit[x]
        x-=x&-x
    return ret

for e,i in enumerate(A):
    add(e+1,i)
for i in range(N):
        print(sum(i))