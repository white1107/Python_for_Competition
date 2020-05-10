def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """5
1 1 2 2 3
2
1 2
"""
input = get_input(INPUT)
#######

def binary_search_loop(data,target):
    left, right = 0, len(data)

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

ans = 0
for t in T:
    if binary_search_loop(S,t):
        ans +=1
    
print(ans)