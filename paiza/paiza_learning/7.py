# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_std_in_out_boss

# 解答例
N = int(input())

for _ in range(N):
    s_a = input().split()
    print(s_a[0], int(s_a[1]) + 1)
printの第一引数、第二引数で入れるとどうなるん？
→print関数 に複数の引数を与えると、受け取った値を半角スペース区切りでまとめて 1 行で出力してくれます。

# 書いたコード
# num = int(input())

# for i in range(num):
#     a = input().split()
#     print(a[0]+ " " + str(int(a[1]) + 1))
    
    

# 1 行目には社員の数を表す整数 N が与えられ、2 行目 〜 (N + 1) 行目の各行では、社員の名前を表す文字列 s_i とその社員の昨年度の年齢を表す整数 a_i が半角スペース区切りで与えられます（1 ≤ i ≤ N）。

# 入力値最終行の末尾に改行が１つ入ります。
# 文字列は標準入力から渡されます。

# 入力された通りの順番で、社員 s_i の名前と、その社員の今年度の年齢を半角スペース区切りでN行出力してください。

# 入力例2
# 3
# Tanaka 18
# Sato 50
# Suzuki 120

# 出力例2
# Tanaka 19
# Sato 51
# Suzuki 121