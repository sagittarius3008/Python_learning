# array = [["勇者","忍者","武士"],["戦士","僧侶","魔法使い"]]
# print(array[1][2])

# item_1 = ["木の棒", "こん棒", "エクスカリバー"]
# item_2 = ["おにぎり", "おにぎり", "むぎ茶"]
# item_3 = ["毒消し", "薬草", "アイアンシールド"]

# basket = [item_1, item_2, item_3]
# print(basket)

# .append:追加, del basket[0]:削除などリストと同様

# letter_A = [[0,0,1,1,0,0],
#             [0,1,0,0,1,0],
#             [1,0,0,0,0,1],
#             [1,1,1,1,1,1],
#             [1,0,0,0,0,1],
#             [1,0,0,0,0,1]]
# 最初のfor文で中のリストを呼ぶ
# for i in letter_A:
#     # 次のfor文で各数字を呼ぶ（そのままだと縦一列）
#     for j in i:
#         if j == 0:
#             # end=""で改行を消す
#             print(" ", end ="")
#         else:
#             print("@", end ="")
#     # この位置でprintすることでリスト毎に改行する
#     print("")


letters = [[[0,0,1,1,0,0],
             [0,1,0,0,1,0],
             [1,0,0,0,0,1],
             [1,1,1,1,1,1],
             [1,0,0,0,0,1],
             [1,0,0,0,0,1]],
            [[1,1,1,1,1,0],
             [1,0,0,0,0,1],
             [1,1,1,1,1,0],
             [1,0,0,0,0,1],
             [1,0,0,0,0,1],
             [1,1,1,1,1,0]],
            [[0,1,1,1,1,0],
             [1,0,0,0,0,1],
             [1,0,0,0,0,0],
             [1,0,0,0,0,0],
             [1,0,0,0,0,1],
             [0,1,1,1,1,0]]]

# ここに、ドットを表示するコードを記述する
# for anime in letters:
#     for line in anime:
#         for dot in line:
#             if dot == 1:
#                 print("@", end="")
#             else:
#                 print(" ", end="")
#         print()
#     print()

# text = ["吾輩は猫である",
#         "名前はまだ無い",
#         "どこで生まれたか",
#         "とんと見当がつかぬ"]

# #ここに、行番号を表示するコードを記述する
# for (i, line) in enumerate(text):
#     print(f"{i+1}:{line}")


# 6-10 不正解！！！！！！！！！
# 初期の地図
# landmap = [["森" for i in range(19)] for j in range(10)]
# landmap[2][9] = "城"
# landmap[0][0] = "町"
# landmap[0][18] = "町"
# landmap[9][0] = "町"
# landmap[9][18] = "町"
# for i, line in enumerate(landmap):
#     for j, area in enumerate(line):
#         # if文を追加する
#         if (i % 9 == 0 or j % 9 == 0) and area == "森":
#             print("＋", end="")
#         else:
#             print(area, end="")
#     print()

# 標準入力から、2次元リストを読み込む
# 標準入力のデータ
# 0,0,1,1,0,0
# 0,1,0,0,1,0
# 1,0,0,0,0,1
# 1,1,1,1,1,1
# 1,0,0,0,0,1
# 1,0,0,0,0,1
# _

# letter_A = []
# while True:
#     line = input()
#     if line == "_":
#         break
#     else:
#         letter_A.append(line.split(","))
# print(letter_A, end = "")


# 2次元リストで画像を表示する

# 画像用リスト
players_img = [
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Empty.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Dragon.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Crystal.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Hero.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Heroine.png"]

# 配置データを読み込み
team = []
while True:
    line = input()
    if line == "_":
        break
    team.append(line.split(","))

# ここから先を入力してください
print("<table>")
for line in team:
    print("<tr>")
    for person in line:
        # fstringだと微妙に余白が狂う？？
        print("<td><img src='" + players_img[int(person)] + "'></td>")
    print("</tr>")    
print("</table>")     