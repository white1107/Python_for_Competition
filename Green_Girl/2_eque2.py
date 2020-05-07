
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """6 3
-6 -100 50 -2 -5 -3
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
        new_A.sort(reverse=True)
        h = K - len(new_A)
        while h >0 and new_A:
            if new_A[-1] > 0:
                break
            else:
                new_A.pop()
                h-=1
        M = max(M,sum(new_A))
print(M)