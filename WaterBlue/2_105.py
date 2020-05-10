
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """7 9
1 2
1 3
2 3
4 5
4 6
4 7
5 6
5 7
6 7
"""
input = get_input(INPUT)
#####################################
import itertools
n,m = map(int,input().split())

M = []

for i in range(m):
    x,y = map(int,input().split())
    M.append((x,y))
ans = 1
for i in range(n,0,-1):
    for II in itertools.combinations(range(1,n+1),i):
        if all((x, y) in M for x, y in itertools.combinations(II, 2)):
            print(i)
            exit()

#####



import itertools
n,m = map(int,input().split())

M = []

for i in range(m):
    x,y = map(int,input().split())
    M.append((x-1,y-1))
ans = 1
for i in range(1,m+1):
    for II in itertools.combinations(range(n),i):
        if all((x, y) in M for x, y in itertools.combinations(II, 2)):
            ans = i
print(ans)
###

import itertools
n,m = map(int,input().split())

M = []

for i in range(m):
    x,y = map(int,input().split())
    M.append((x-1,y-1))
ans = 1
for i in range(1,n+1):
    for II in itertools.combinations(range(n),i):
        D = []
        for I in itertools.combinations(II,2):
            D.append(I)
        if len(set(D)&set(M)) == len(D):
            ans = i
print(ans)


#####################################

import itertools
 

N, M = map(int, input().split())  # N人, 関係M個
relations = [tuple(map(int, input().split())) for _ in range(M)]
 
ans = 1
for i in range(1, N+1):
    for j in itertools.combinations(range(1, N + 1), i): 
        M = list(itertools.combinations(j, 2)) # j人の議員から2り選ぶ組が全部relralationとあっているか
        if set(M)&set(relations) == len(set(M)):ans = i
print(ans)