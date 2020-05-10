def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """3
"""
input = get_input(INPUT)
#######
n = int(input())
dp = [0]*(n+1)
dp[0] = dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])


