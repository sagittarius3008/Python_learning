# 解答例
N = int(input())

for i in range(N):
    [t, h, m] = input().split() # ['13:00', '1', '30']
    th = int(t[:2]) # 13
    tm = int(t[3:]) # 0
    h = int(h)# 1
    m = int(m)# 30

    ah = th + h
    am = tm + m

    if am >= 60:
        ah += 1
        am -= 60
    if ah >= 24:
        ah -= 24

    ah = str(ah)
    am = str(am)

    if len(ah) == 1:
        ah = "0" + ah
    if len(am) == 1:
        am = "0" + am

    print(ah + ":" + am)

# 書いたコード
# count = int(input())

# # 日付を調整
# def time_change(h, s):
#     if s >= 60:
#         h += 1
#         s -= 60
#         if h >= 24:
#             h -= 24
#     else:
#         if h >= 24:
#             h -= 24
#     if len(str(h)) == 1:
#         h = "0" + str(h)
#     if len(str(s)) == 1:
#         s = "0" + str(s)
#     print(str(h) + ":" + str(s))
    

# while count > 0:
#     attr = input().split() # 複数回入力を受ける
#     time_change(int(attr[0][:2]) + int(attr[1]) ,int(attr[0][3:])+ int(attr[2]))
#     count -= 1