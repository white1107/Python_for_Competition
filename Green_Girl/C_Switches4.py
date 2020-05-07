
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2 3
2 1 2
1 1
1 2
0 0 1
"""
input = get_input(INPUT)
#####################################
N, M = list(map(int, input().split()))
s = []
for i in range(M):
    tmp = list(map(int, input().split()))
    t = 0
    for j in tmp[1:]:
        t += 1 << (j - 1)
    s.append(t)
p = list(map(int, input().split()))

ans = 0
for x, y in zip(s, p):
    for i in range(1 << N):
        print(i,x)
        t = i & x
        c = bin(t).count('1') % 2
        if c == y:
            print(1,x,y)
            ans +=1
            break
print(ans)


