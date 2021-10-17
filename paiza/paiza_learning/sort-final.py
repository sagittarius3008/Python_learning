# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_sort_boss
# 1行目が以下の出力数。
# 2行目以降を逆順に並べ替えよ。
# 与える数字は二つずつで、先頭が同じ数字の場合のみ二つ目を参照する。

# 入力例2
# 4
# 2 3
# 0 4
# 5 0
# 3 3

# 出力例2
# 0 4
# 3 3
# 2 3
# 5 0

# num = int(input())

# lis = []
# for i in range(num):
#     a =list(map(int, input().split()))
#     lis.append(a)


# # print(lis)
# lis.sort(reverse=True)
# # print(lis)

# for i in range(num):
#     for x,j in enumerate(lis[i]):
#         if x == 0:
#             print(j, end = " ")
#         else:
#             print(j)

# ～～～～～～～～～～～～～～～

# num = int(input())

# lis = []
# for i in range(num):
#     a =list(map(int, input().split()))
#     lis.append(a)

# # print(lis)
# lis.sort(reverse=True)
# # print(lis)

# for i in range(num):
#     a,b =lis[i]
#     print(str(a) +" "+ str(b))
    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# 模範解答
N = int(input())
kingin = [0] * N

for i in range(N):
    [a, b] = [int(j) for j in input().split()]
    kingin[i] = [b, a]
# print(kingin) # [[3, 2], [4, 0], [0, 5], [3, 3]]
# bでソート
kingin.sort(reverse=True)

# 表示はaを前に
for i in range(N):
    [a, b] = kingin[i]
    print(b, a)