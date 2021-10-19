# 最終行と同じ名前で対応する数字を表せ

# 入力
# 2
# Kirishima 1
# Kyoko 2
# Kirishima

n = int(input())
zaisan = {} # 辞書型の初期化

for i in range(n):
    [s, a] = input().split()
    zaisan[s] = a # 一週目：{'Kirishima': '1'} 二週目：{'Kirishima': '1', 'Kyoko': '2'}
S = input()

print(zaisan[S]) # => 1