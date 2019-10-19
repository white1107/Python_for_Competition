def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """6 1
350 350 70 2 3 4"""
input = get_input(INPUT)

###############################
a,b = map(int,input().split())
import bisect
A= a +1
B = b+1
# d = [[0]*B for i in range(A)]
l = []
for i in range(b):
    tl = list(map(int,input().split()))
    l.append(tl)
for i in range(b):
    for j in range(1,a):
        l[i][j] += l[i][j-1] 
for i in range(a):
    for j in range(1,b):
        l[i][j] += l[i-1][j]
f = 0
for i in range(b):
    for j in range(a):
        d = l[i][j - 777
        if d < 0:continue
        if d == 0: F = 1
        k = bisect.bisect_left(l[])



# insert_index = bisect.bisect_left(a,x)
# l = [[0]*10 for i in range(10)]
# print(l)
