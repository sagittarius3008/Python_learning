# team = ["勇者", "魔法使い", 100]
# print(team)

# list = ["戦士","侍","僧侶","魔法使い"]
# print(list)

# item = ["ロングソード", "ブレードソード", "エクスカリバー"]
# print(item)
# print(item[0])
# num = 0
# print(item[num + 1])

# len関数
# print(len(item))

# item.append("蜻蛉切")
# print(len(item))
# item[3] = "蜻蛉切改"

# リストの要素の削除
# item.pop(2)

# for文との組み合わせ
# for i in item:
    # print(i)

# print("<select name = 'weapon'>")
# for weapon in item:
#     print("<option>" + weapon + "</option>")
# print("</select>")

# line = input().rstrip().split(",")
# print(line)
# print(len(line()))

# str = "One cold rainy day when my father was a little boy he met an old alley cat on his street"
# word = str.split(" ")
# print(len(word))

# 複数行データのinput/行数が分からない場合
# import sys
# array = []
# for line in sys.stdin.readlines(): //stdin = standartd input(=キーボードからの入力受付)
#     array.append(line.rstrip())

# print(array)



# import random
# line = input().rstrip()
# janken = line.split(",")
# num = len(janken)
# print(janken)
# print(janken[random.randrange(num)])

# sortedメソッド：リストの整列（文字コード順）
# weapons = ["イージス","ウィンド","アース","イナズマ"]
# print(sorted(weapons))
# print(sorted(weapons,reverse=True)) # 逆順

apples = [310, 322, 292, 288, 300, 346]
print(sorted(apples,reverse = True))

words = ["pumpkin", "orange", "apple", "carrot", "onion"]
# ここに、要素をソートして表示するコードを記述する
print(sorted(words))