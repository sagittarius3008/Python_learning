# 3桁になるまで先頭に0を追加
# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_string_step4

# 解答例
n = input()

while len(n) < 3:
    n = "0" + n

print(n)


書いたコード
num = input()

if len(num) == 3:
    print(num)
elif len(num) == 2:
    print("0" + num)
else:
    print("00" + num)