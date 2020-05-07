
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3 2
5 1 4
2 3
1 5
"""
input = get_input(INPUT)
#####################################
N,M=map(int,input().split())
A = list(map(int,input().split()))
l = [] 
for i in range(M):
  tmp = list(map(int,input().split()))
  l.append([tmp[1],tmp[0]])
l.sort(reverse=True)
for i,j in l:
    A.extend([i]*j)
    if len(A)>2*N:break
A.sort(reverse=True)
print(sum(A[:N]))