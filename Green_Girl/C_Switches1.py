
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
k = []
for i in range(m):
        tmp = list(map(int,input().split()))
        k.append(tmp[1:])
p = list(map(int,input().split()))

res = 0
for i in range(2 ** n):
        l = []
        for j in range(n):
                print(i & (2 ** j),i,2**j)
                l.append(int((i & (2 ** j)) == 0))
