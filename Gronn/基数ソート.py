def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """32
3 1 4 1 5 9 2 6 5333 33 35 28 911 27 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5
"""

input = get_input(INPUT)
#################
from collections import defaultdict
from copy import copy

D1 = defaultdict(list)
N = int(input())
A = list(map(int,input().split()))

M = len(str(max(A))) #最大桁数の取得

ans = []
print(M)
for i in range(M+1):
    if i == 0:
        for j in A:
            D1[j%10].append(j)
    else:
        for I in range(10):
            for j in tmpD[I]:
                D1[(j%10**(i+1))//(10**(i))].append(j)
                if i == M-1:ans.append(j)
    print(i,D1)      
    tmpD = copy(D1)
    D1 = defaultdict(list)
ans = D1[0]
print(ans)
