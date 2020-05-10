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

INF = 10**9 + 1
n = int(input())
dp = [INF] * (n+1)

for _ in range(n):
    a = int(input())
    i = bisect_left(dp, a)
    dp[i] = a
    # print(dp)

print(bisect_left(dp, INF))