
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2
1 1
2 2
"""
input = get_input(INPUT)
#####################################
n = int(input())
M = []
for i in range(n):
    x,y = map(int,input().split())
    M.append([x,y])
