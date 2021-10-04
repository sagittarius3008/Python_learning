# class Greeting: #大文字
#     # クラス内のメソッド定義にはselfをつける（インスタンス変数を使うのに必要）
#     # オブジェクトの呼び出し
#     def say_hello(self):
#         print("hello paiza")

# greeting = Greeting()
# greeting.say_hello()

# # 8-3-2 不正解！！！！
# class Greeting:
#     # コンストラクタ・一番始めに読み込まれる
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print("hello " + self.name)

# he = Greeting("paiza") # コンストラクタのnameにpaizaが代入されてる
# he.say_hello()



# class Enemy:
#     def __init__(self, name):
#         self.name = name

#     def attack(self):
#         print(self.name + "は勇者を攻撃した")

# enemies = []
# enemies.append(Enemy("スライム"))
# enemies.append(Enemy("モンスター"))
# enemies.append(Enemy("ドラゴン"))

# for enemy in enemies:
#     enemy.attack() # enemy の中身はEnemy("スライム")


# 小数点切り捨てについて
# 今回は、int関数を用いて、小数点以下を切り捨てました。
# 切り捨て以外にも、mathモジュールを用いると、様々な方法で、小数から整数に変換できます。

# 例えば、trunc(x)は、int関数と同様に、xの小数部分を削除します。
# ceil(x)は、x以上の最小の整数を返します。天井関数と呼ばれています。
# floor(x)は、x以下の最大の整数を返します。床関数と呼ばれています。
# round(x)は、端数が0.5より大きいならは切り上げ、端数が0.5より小さいなら切り捨てた整数を返します。
# ただし、端数がちょうど0.5の場合、切り捨てと切り上げのうち、結果が偶数になる整数を返します。
# 一般的な四捨五入と異なる動作をするので注意が必要です。

# round関数については、下記URL先をご参照ください。
# https://docs.python.jp/3/library/functions.html?highlight=round#round

# mathモジュールについて、詳しくは、下記URL先をご参照ください。
# https://docs.python.jp/3/library/math.html

# class Item:
#     tax = 1.08

#     def __init__(self, price, quantity):
#         self.price = price
#         self.quantity = quantity

#     def total(self):
#         return int(self.price * self.quantity * Item.tax)

# apple = Item(120, 15)
# total = apple.total()
# print("合計金額は" + str(total) + "円です")

# orange = Item(85, 32)
# print("合計金額は" + str(orange.total()) + "円です")


text = "pYthon"
print(text)
# capitalizeメソッド：先頭の文字を大文字、あと小文字
print(text.capitalize())
print(text.upper())

players = "勇者,戦士,魔法使い,忍者"
list = players.split(",")　# リスト化
print(list)
list.remove("忍者") # リストから削除
print(list)
list.append("霧島") # リストに追加
print(list)


# msg = input()
# if msg == msg.lower():
#     print("True")
# else:
#     print("False")

# 模範解答
# islower(): 文字列中の文字全てが小文字ならTrueを返す
# print(msg.islower())

# insert(i, x): インデックス i に、要素 x を挿入する。
# team = ["勇者", "戦士", "魔法使い", "忍者"]
# team.insert(3,"盗賊")
# print(team)

# __メソッド名：プライベートメソッド（クラス内でしか使えない）

# __変数名：プライベート変数（クラス内でしか使えない）
class Player:
    def __init__(self, job, weapon):
        self.job = job
        self.__weapon = weapon

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        self.__attack("スライム")

    def __attack(self, enemy):
        print(self.__weapon + "で" + enemy + "を攻撃")


player1 = Player("戦士", "剣")
player1.walk()
# player1.__attack("スライム")
# print(player1.__weapon)