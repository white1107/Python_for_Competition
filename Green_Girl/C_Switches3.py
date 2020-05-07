
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5 2
3 1 2 5
2 2 3
1 0
"""
input = get_input(INPUT)
#####################################
import itertools
N,M = map(int,input().split())
s = []
for i in range(M):
    dp = [0]*(N)
    tmp = list(map(int,input().split()))
    for j in tmp[1:]:dp[j-1]=1
    s.append(dp)
p = list(map(int,input().split()))
ans = 0

for i in itertools.product([0, 1], repeat=N):
    tmp = 0
    dp = [0]*M
    for I in range(M):
        for j in range(N):
            dp[I] += s[I][j] * i[j]
    for e,i in enumerate(dp):
        dp[e] = i%2
    if dp == p:
        ans+=1
print(ans)
