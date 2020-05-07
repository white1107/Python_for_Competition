def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
2 2 3 6
2 2 2 2
1 1 4 7
3 5 4 7
"""
input = get_input(INPUT)
#####################################

from heapq import heappush, heappop

H,W= map(int,input().split())
Q = int(input())

pint = [[0]*(W+1) for _ in range(H+1)]

class Bit2D:
    def __init__(self,H,W):
        self.bit = [[0]*(W+1) for _ in range(H+1)]
    def add(self,a,b,Z):
        if a > H :print('Hell')
        if b > W :print('Hell')
        x = a
        while x<=H:
            y = b
            while y<=W:
                # print(x,y)
                self.bit[x][y]+=Z
                y+=y&-y
            x+=x&-x
    def s_sum(self,a,b):
        # print('strat',a,b)
        ret = 0
        x = a
        while x>0:
            y = b
            while y>0:
                # print(x,y)
                ret+=self.bit[x][y]
                y-=y&-y
            x-=x&-x
        return ret

    def ssum(self,x1,y1,x2,y2):
        return self.s_sum(x2,y2) - self.s_sum(x1-1,y2) - self.s_sum(x2,y1-1) + self.s_sum(x1-1,y1-1)
    
    def pprint(self):
        for i in self.bit:
            print(i)
    
    def psum(self,x1,y1,x2,y2):
        return [self.s_sum(x2,y2) , self.s_sum(x1-1,y2) , self.s_sum(x2,y1-1) , self.s_sum(x1-1,y1-1)]


q = []
J = Bit2D(H,W)
O = Bit2D(H,W)
I = Bit2D(H,W)


for i in range(H):
    tmp = input()
    tmp = list(tmp)
    for e,j in enumerate(tmp):
        if j == 'J':J.add(i+1,e+1,1)
        if j == 'O':O.add(i+1,e+1,1)        
        if j == 'I':I.add(i+1,e+1,1)

for i in range(Q):

    h1,w1,h2,w2 = list(map(int,input().split()))
    print(J.ssum(h1,w1,h2,w2),O.ssum(h1,w1,h2,w2),I.ssum(h1,w1,h2,w2))
