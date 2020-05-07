
def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT = """32
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5
"""
input = get_input(INPUT)
#####################################

N =  int(input())#配列の大きさを取得
A = list(map(int,input().split()))

dp = [0]*(N+1)#辞書の用意

ans = []#答えの配列

for i in A:#出現した要素をカウント
    dp[i]+=1

for i in dp:#並び替え実行部分
    for j in range(i):#出現回数分追加してあげる
        ans.append(i)
