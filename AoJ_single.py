def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3"""
input = get_input(INPUT)
###############################
from heapq import heappush, heappop
INF = 10**10
a = int(input())
d = [[] for i in range(a)]
for i in range(a):
    tl = list(map(int,input().split()))
    ta , tb = tl[0],tl[1]
    t = 2
    for j in range(tb):
        tta,ttb = tl[t],tl[t+1]
        d[i].append((tta,ttb))
        t+=2

def dijkstra(N, G, s):
    dist = [INF] * N
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in G[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    for i in range(a):
        print(str(i)+" "+str(dist[i]))
dijkstra(a,d,0)
