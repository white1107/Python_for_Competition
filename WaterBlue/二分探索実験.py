def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """4
5 6
12 4
14 7
21 2
"""
input = get_input(INPUT)
#######
n = int(input())
HS = [list(map(int, input().split())) for _ in range(n)]

l = 0
r = 10 ** 18

while r - l > 1:
  m = (l + r) // 2
  li = sorted([(m - h) // s for h, s in HS])
  if all([t >= i for i, t in enumerate(li)]):
    r = m
  else:
    l = m
print(r)
