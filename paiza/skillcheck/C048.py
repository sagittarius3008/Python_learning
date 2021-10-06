# ・一度飲むと2杯目はP% off。かつ、値下げが累積される。
# ・毎回の値下げにおいて小数点以下切り捨て。
# ・ただで飲めるようになるまではいくらかかるか。

# 入力例2
# 1000 99
# 出力例2
# 1010

import math # math.floor()切り捨てのメソッドを使うためにimport

math.floor(1.2)
[a, b] = input().split()
ans = 0

while int(a) != 0: # ここを == 0にしてしまって詰まった
    ans += int(a)
    a = int(a) * (100-int(b)) /100
    math.floor(a)

print(ans)