# type,idの表示
print(type("hello"))
print(type(1))
print(id(1))

# int型
print(type(-1))

# float(浮動小数点)
print(type(1.5))
print(0.1 + 0.2 + 0.3) #正確に0.6にはならない

# 型変換と足し算
result = int("1") + 3
print(result)
# True = 1, False =0として
result = True + 3
print(result)