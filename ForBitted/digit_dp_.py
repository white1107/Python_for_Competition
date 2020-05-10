

S = input()
l = list(S)
s = len(S)

dp[0][0][0] = 1
for i in range(s):
    for smaller in range(2):
        for j in range(2):
            for x in range(l[])