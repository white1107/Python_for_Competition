
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

n,m = map(int,input().split())
l = [list(map(int,input().split()))[1:] for _ in range(m)]
p =list(map(int,input().split()))
r = 0
for i in range(2**n):
    t = [0] * m
    for j in range(n):
        if 2**j & i:
            for k in range(m):
                if j in l[k]:
                    t[k] ^= 1
    if p == t:
        r += 1

print(r)
