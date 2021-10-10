# m = int(input())
# c = [""] * m    # ex) m = 4, c = ['', '', '', '']

# 有無を確認すべきアルファベットのリスト
# for i in range(m):
#     c[i] = input()

# n = int(input())
# S = [""] * n

# 調べる単語リスト
# for i in range(n):
#     S[i] = input()

# for i in range(m):
#     for j in range(n):
#         if c[i] in S[j]:
#             print("YES")
#         else:
#             print("NO")


lang_count = int(input()) # input()
lang = []
for i in range(lang_count): # lang_count
    lang.append(input())
# lang = ['c', 'd']

count = int(input())

for i in lang:
    for j in range(count):
        ans = input()
        
        if i in ans:
            print("YES")
        else:
            print("NO")