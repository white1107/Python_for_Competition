
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
N,M = list(map(int, input().split()))
S = []
for i in range(M):
    tmp = list(map(int, input().split()))
    t = 0
    for j in tmp[1:]:
        t += 1 << (j - 1)
    S.append(t)
P = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
    f = 0
    for s, p in zip(S, P):
        t = i & s
        c = bin(t).count('1') % 2
        if c == p:f+=1
    if f == M:
        ans += 1
print(ans)
