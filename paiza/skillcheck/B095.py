[num, length] = input().split()

# 減点を返す
def score(correct, entry):
    minus = 0
    if abs(correct - entry) <= 5:
        minus += 0
    elif abs(correct - entry) <= 10:
        minus += 1
    elif abs(correct - entry) <= 20:
        minus += 2
    elif abs(correct - entry) <= 30:
        minus += 3
    else:
        minus += 5
    return minus
        

# 正解のリストを作る
correct_box = []
for i in range(int(length)):
    correct_box.append(input())


# N人M列の2次元配列を作る
all_box = []
for i in range(int(num)):
    box = []
    for j in range(int(length)):
        box.append(input())
    all_box.append(box)

# 一番高い点数を表示
# 点数を配列化してmax関数使うべきだった・・・！
high = 0
for i in range(int(num)):
    mns = 0
    for (x, j) in enumerate(all_box[i]):
        ans =score(int(correct_box[x]), int(j))
        mns += ans
    total_score = 100 - mns
    
    if total_score > high:
        high = total_score
print(high)