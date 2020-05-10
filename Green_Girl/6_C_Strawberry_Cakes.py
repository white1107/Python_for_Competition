
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """13 21 106
.....................
.####.####.####.####.
..#.#..#.#.#....#....
..#.#..#.#.#....#....
..#.#..#.#.#....#....
.####.####.####.####.
.....................
.####.####.####.####.
....#.#..#....#.#..#.
.####.#..#.####.#..#.
.#....#..#.#....#..#.
.####.####.####.####.
.....................
"""
input = get_input(INPUT)
#####################################
h,w,k = map(int,input().split())
s = []
m = []
for i in range(h):
    tl = input()
    s.append(tl)
c = 0
f = 1
hhh = 1
for e,i in enumerate(s):
    if "#" in i:
        c+=1
        M = [0]*w 
        M[0] = c
        f = 1
        for E,j in enumerate(i):
            if E == 0:
                if j == '.':
                    f=0
                # print(2)
            elif j == '#':
                c+=f
                f = 1
            M[E]=c
        for i in range(hhh):m.append(M)
        hhh =1
    else:
        hhh+=1
for i in range(hhh-1):m.append(M)

for i in m:
    print(*i)
