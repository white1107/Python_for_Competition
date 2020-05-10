
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3
.....................
"""
input = get_input(INPUT)
#####################################
# s = int(input())

# m = 10**9
# x = (m-s%m)%m
# y = (s+x)//m
# print(0,0,m,1,x,y)

s = int(input())

m = 10**9
x = m-s%m
y = (s+x)//m
print(0,0,m,1,x,y)