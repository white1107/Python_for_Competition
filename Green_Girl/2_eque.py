
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """6 4
-10 8 2 1 2 6
"""
input = get_input(INPUT)
#####################################
import heapq 

N,K = map(int,input().split())
A = list(map(int,input().split()))
m = min(N,K) #KがNより大きい場合を防ぐ
M = 0 
for i in range(m+1):
    for j in range(m-i+1):
        A1 = A[:i] #前から取る
        A3 = A[N-j:] #後ろから取る
        new_A = A1+A3
        heapq.heapify(new_A)
        h = K - len(new_A)
        while new_A  and h >0:
            q = heapq.heappop(new_A)
            h-=1
            if q > 0:
                heapq.heappush(new_A,q)
                break
        M = max(M,sum(new_A))
print(M)