def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """6
100 1
100 1
100 1
100 1
100 1
1 30
"""
input = get_input(INPUT)
#######
