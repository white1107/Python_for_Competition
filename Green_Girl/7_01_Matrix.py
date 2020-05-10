
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """2 5 0 0
.....................
"""
input = get_input(INPUT)
#####################################
h,w,a,b = map(int,input().split())
S = '0101'
if a == b == 0:
    for i in range(h):
        print('0'*w)
elif a == b == 1 and h == w:
    for i in range(h):
        for j in range(w):
            if i == j:print('1',end="")
            else:print('0',end="")
        print("")

elif h//2 == b and w//2 == a:
    for i in range(h):
        if i%2==0:print(S[:2]*(w//2)+S[0]*(w%2==1))
        else:print(S[1:3]*(w//2)+S[1]*(w%2==1))