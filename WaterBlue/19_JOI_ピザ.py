def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """20
4
4
12
8
16
7
7
11
8
"""
input = get_input(INPUT)
#######
from bisect import bisect_left,bisect_right

a = int(input())
b = int(input())
c = int(input())
B = [0]
C = []
for i in range(b-1):
    B.append(int(input()))
B.append(a)
ans = 0
B.sort()
# print(B)
for i in range(c):
    cc = int(input())
    t = bisect_right(B,cc)
    ans +=min(cc-B[t-1],B[t]-cc)
print(ans)

