def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3
3 2 1
2 2 1
1 1 1
3
1
4
9
"""
input = get_input(INPUT)
#####################################
a = int(input())
l = []
A = a+1
d = [[0]*A for i in range(A)]
D = [0]*10010
for i in range(a):
    l.append(list(map(int,input().split())))


for x in range(a):
    for y in range(a):
        d[x+1][y+1] = d[x][y+1] + d[x+1][y] - d[x][y] + l[x][y]

for x in range(a):
    for xx in range(x+1,A):
        for y in range(a):
            for yy in range(y+1,A):
                area = (xx - x) * (yy - y)
                S= d[xx][yy] - d[xx][y] - d[x][yy] + d[x][y]
                D[area] = max(S,D[area])
# for i in range(a**2):
#     D[i+1] = max(D[i+1],D[i])
# print(D[:10])
b = int(input())
for i in range(b):
    tmp = int(input())
    print(D[tmp])
