def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4 8
4 2
5 2
2 1
8 3
"""
input = get_input(INPUT)
#######
N,W = map(int,input().split())

dp = [0]*(W+1)
L = []
for i in range(N):
    v,w = map(int,input().split())
    L.append([v,w])

for i in range(N):
    for w in range(W+1):
        if w-L[i][1]>=0 :dp[w] = max(dp[w],dp[w-L[i][1]]+L[i][0])
print(dp[-1])