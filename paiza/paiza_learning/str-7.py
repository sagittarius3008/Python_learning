# 入力された時間に+30分せよ

# 解答例(24時超える処理は行われていない)
S = input()
h = int(S[:2])
m = int(S[3:])

if m + 30 >= 60:
    h = str(h + 1)
    m = str(m + 30 - 60)
else:
    h = str(h)
    m = str(m + 30)

if len(h) == 1:
    h = "0" + h
if len(m) == 1:
    m = "0" + m

print(h + ":" + m)


# 書いたコード（24時を超える、60分を超える処理が上手くできていない）

# time = input()
# h = time[:2]
# s = int(time[3:]) + 30

# def time(h,s):
#     print(str(h) + ":" + str(s))


# if s >= 60:
#     h = int(h) + 1
#     if h > 24:
#         h = 0
#         time(h,s)
#     else:
#         time(h,s)
# else:
#     time(h,s)
    