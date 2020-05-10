def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5
5
1
3
2
4
"""
input = get_input(INPUT)
#######
from bisect import bisect_left

N = int(input())
dp = []
append = dp.append
result = -1
A= []
for i in range(N):
    a = int(input())
    A.append(a)
for a in A:
    i = bisect_left(dp, a)
    if i > result:
        append(a)
        result += 1
    else:
        dp[i] = a

    print(dp)
print(result+1)