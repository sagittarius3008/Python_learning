# 正答率8割
# ランタイムエラー、出力エラーあり
import math
a = input()
m = a[0:2]
d = int(a[3:5])
h = a[6:8]
t = a[9:11]


if int(h) >= 24:
    pl = math.floor(int(h)/24)
    h = int(h) - pl * 24
    if len(str(h)) == 1:
        h = "0" + str(h)
    d += pl

print(m + "/" + str(d) + " " + h + ":" + t )