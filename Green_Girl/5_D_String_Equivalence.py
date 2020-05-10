def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """10
"""
input = get_input(INPUT)
#######
a = int(input())
S = 'abcdefghij'

def dfs(s,c):
    if c == a:
        ans.append(s)
        return 
    for i in S[:c+1]:
        if i in s:dfs(s+i,c+1)
        else:
            dfs(s+i,c+1)
            return 
ans = []

dfs("",0)

for i in ans:
    print(i)