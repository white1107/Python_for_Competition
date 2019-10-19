
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4 6 1
0 1 1
0 2 4
2 0 1
1 2 2
3 1 1
3 2 5"""
input = get_input(INPUT)
###############################
from heapq import heappush, heappop
INF = 10**10
a,b,c = map(int,input().split())
d = [[] for i in xrange(a)]
for i in range(b):
    ta,tb,tc = map(int,input().split())
    d[ta].append((tb,tc))

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
        print(dist[i] if dist[i] < INF else "INF")
dijkstra(a,d,c)

