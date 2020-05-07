
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5
3 1 2 5 4
"""
input = get_input(INPUT)
#####################################

n = int(input())
A = list(map(int,input().split()))
N = len(A)
class BIT:
    def __init__(self,N):
        self.bit = [0]*(N+1)
    def add(self,a,w):
        x = a
        while x<=N:
            self.bit[x]+=w
            x+=x&-x
    def sum(self,a):
        ret = 0
        x = a
        while x>0:
            ret+=self.bit[x]
            x-=x&-x
        return ret
b = BIT(N)
ans = 0
for e,i in enumerate(A):
    print('PHase')
    print(e,i,ans,b.sum(i))
    ans += e-b.sum(i)
    b.add(i,1)



    
if (n-ans)%2==0 :
    print('YES')
else:
    print('NO')
