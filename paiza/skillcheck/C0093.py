# 1桁目と2桁目の数字を足して出た数字の1桁目を比較する。
# 83 96 だったら11と15、1と5で右（Bob）が勝ち。
変数名は怪しいけど比較的わかりやすくかけた
[Bob, Alice] = input().split()

Bscore = int(Bob[0]) + int(Bob[1])
Ascore = int(Alice[0]) + int(Alice[1])

A = int(str(Ascore)[-1])
B = int(str(Bscore)[-1])

if A > B:
    print("Alice")
elif A < B:
    print("Bob")
else:
    print("Draw")
    