def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2 20
5 9
4 10
"""
input = get_input(INPUT)
#######
N,W = map(int,input().split())

dp = [[0]*(W+1) for _ in range(N+1)]
L = []
for i in range(N):
    ta,tb = map(int,input().split())
    L.append([ta,tb])

for i in range(N):
    for w in range(W+1):
        if w-L[i][1]>=0 :dp[i+1][w] = max(dp[i][w],dp[i+1][w-L[i][1]]+L[i][0])
        else: dp[i+1][w] = dp[i][w]
print(dp[-1][-1])
print(dp)