# dictionary型
# enemyDict = {"zako":"slime","boss":"dragon"}
# print(enemyDict)
# print(enemyDict["boss"])
# level = "boss"
# print(level)


statuses ={"職業":"1戦士","体力":"3大","魔法力":"2小","ゴールド":"4たんまり"}
# キーでソート
print(sorted(statuses))
# 値とセットにしてソート
print(sorted(statuses.items())) #turple化される
# 追加
statuses["技"] = "メタル切り"
print(len(statuses))
statuses["魔法力"] = "500"
# 削除
del statuses["魔法力"]
print(statuses)
print(statuses["職業"])

# for文で値を取り出す
# print(i)だとキーが取れる
for status in statuses:
    print("おぬしのステータスは" + statuses[status] + "じゃ")

# itemsメソッド：キーと値を両方取り出す
skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
for (key, value) in skills.items():
    print(f"{key}は{value}です")

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
for i in points:
    sum += points[i]
print(sum)

# リストと辞書の組み合わせ
# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
# items_orders = ["剣", "盾", "回復薬", "クリスタル"]

# for item_name in items_orders:
#     print("<img src=" + items_imges[item_name] + "><br>")

# 複数受け取った値を画像出力する。
import sys
array = []
for line in sys.stdin.readlines():
    array.append(line.rstrip())

for item in array:
    if item in items_imges:
        print("<img src=" + items_imges[item] + "><br>", end = "") #改行したくないのに改行される…？

# 入力値↓　（そもそも一番目の入力が入力数を表すことを読んでなかった…）
# 6
# 回復薬
# 盾
# クリスタル
# クリスタル
# 剣
# 剣

# 模範解答
item_cnt = int(input())

while item_cnt > 0:
  item = input()
  print("<img src = '" + items_imges[item] + "'>")
  item_cnt = item_cnt - 1