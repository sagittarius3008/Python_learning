# 関数の定義
# def say_hello():
#     print("hello paiza")

# # この下に関数呼び出しを記述す
# say_hello()


# 九九の表を作成してみよう

# def multiply(x, y):
#     return x * y


# count = 1
# while count < 10:
#     for num in range(1, 10):
#         print(multiply(count, num), end="")
#         if num < 9:
#             print(", ", end="")
#     count += 1
#     print("")

# # 模範解答
# for step in range(1, 10):
#     for num in range(1, 10):
#         print(multiply(step, num), end="")
#         if num < 9:
#             print(", ", end="")
#     print("")

# グローバル変数(ｖｓ　ローカル変数)基本的に変更不可

# msg = "hello"

# def say_hello():
#     # 宣言しないと変更不可（そも使用は非推奨）
#     global msg
#     msg += " "
#     msg += "paiza"
#     print(msg)

# say_hello()


# RPGの攻撃シーン

# def attack(person):
#     print(person + "はスライムを攻撃した")

# def output_enemy_hp(enemy_hp):
#     print("敵のHPは残り" + str(enemy_hp) + "です")

# enemy_hp = int(input())
# team = {"勇者" : 200, "戦士" : 150, "魔法使い" : 100}

# for person, power in team.items():
#     attack(person)
#     # 以下に、敵の体力を減少させるコードを書く
#     enemy_hp -= power
#     output_enemy_hp(enemy_hp)


# # 引数のデフォルト値
# def say_hello(target = "paiza"):
#     print("hello " + target)

# # この下に関数呼び出しを記述する
# say_hello("paiza")

# 可変長引数 *でいくつでも取れるように設定してfor文で一つずつ出している
# def battle(*enemies):
# 	for enemy in enemies:
# 		print("戦士は" + enemy + "と戦った")

# battle("スライム", "モンスター", "ドラゴン")

# 可変長引数：辞書型
# def introduce(**people):
#     for name, greeting in people.items():
#         print("私は" + name + "です。" + greeting)

# introduce(hero = "はじめまして", villager = "こんにちは", soldier = "よろしくお願いします")

# キーワード引数
# def introduce(name = "私は", role = "村人"):
#     print(name + role + "です")
# introduce()

# 引数の省略（片方だけ指定するパターン）
def introduce(name = "私は", role = "村人"):
    print(name + role + "です")

introduce(role="戦士")