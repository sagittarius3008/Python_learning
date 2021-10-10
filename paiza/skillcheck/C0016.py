# ある単語に該当の文字があった場合、指定の文字に入れ替えろ。

word = list(input())

# 何番目の文字に該当したかが分かれば、word_list[i]の形で入れ替えができるはず…。
# が、分からん。in演算子は何番目か、まではサポートしてなさそう。
# forループ回して一つ一つ確認して合致したところでbreakさせても余計に手数がかかる。
# # ["O","I","Z","E","A","S","G"] = [0,1,2,3,4,5,6]

# word_list = ["O","I","Z","E","A","S","G"]

# for i in word:
#     # print(i)
#     if i in word_list:
#         # print(word_list)
        

for i in word:
    if i == "A":
        print("4", end = "")
    elif i == "E":
        print("3", end = "")
    elif i == "G":
        print("6", end = "")
    elif i == "I":
        print("1", end = "")
    elif i == "O":
        print("0", end = "")
    elif i == "S":
        print("5", end = "")
    elif i == "Z":
        print("2", end = "")
    else:
        print(i, end = "")