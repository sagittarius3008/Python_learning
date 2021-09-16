# 同じオブジェクトか判定する(idベース)
a = 1
b = 1
c = 3
print(id(1))
print(id(a))
print(id(b))
print(a is b)
print(a is not c)

# 文字列
hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"
print(id(hello))
print(id(hello2))

# noneの判定

nothing = None
print(nothing is None)