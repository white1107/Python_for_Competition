
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
N,K = map(int,input().split())
A = list(map(int,input().split()))

q = []
s = 0
ans = 0
c = 0
for e,i in enumerate(A):
    q.append(i)
    s+=i
    while s>=K:
        s-=q[c]
        ans+=N-e
        c+=1
print(ans)
