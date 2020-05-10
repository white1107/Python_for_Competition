
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5 9
0 0
"""
input = get_input(INPUT)
#####################################


while 1:
    n,x = map(int,input().split())
    if x+n == 0:
        break
    else:
        ans = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if i+j+k == x:
                        ans +=1
        
        print(ans)