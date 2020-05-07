
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352
"""
input = get_input(INPUT)
#####################################
import bisect

N,K = map(int,input().split())
A = list(map(int,input().split()))
S = [0]
for i in A:
    S.append(S[-1]+i)
ans = 0
for i in S:
    ans += N-bisect.bisect_left(S,i+K)+1
print(ans)
