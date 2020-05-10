def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2
1 5
2 4
3 6
"""
input = get_input(INPUT)
#######
from bisect import bisect_left,bisect_right

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
cns = 0
for i in B:
    x = bisect_left(A,i)
    y = bisect_right(C,i)
    y = n - y
    ans += x*y
print(ans)


