# 親が勝ったときがHigh
# 一枚目同士を比較 → High or Low
# 同値だったら二枚目を比較 → 親が小さいとHigh

# 入力例
# 7 3 # 親カードの組み合わせ
# 4   # 子の出力枚数
# 7 1 # 子カードの組み合わせ
# 7 4
# 5 3
# 10 1

# 出力例
# Low
# High
# High
# Low


[a, b] = input().split()

for i in range(int(input())):
    [c, d] = input().split()
    if int(a) > int(c):
        print("High")
    elif int(a) == int(c):
        if int(b) > int(d):
            print("Low")
        else:
            print("High")
    else:
        print("Low")
        
    