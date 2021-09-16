# \nで改行
print("hello \nworld")

greeting = "hello"+"world"
yeah = "!!"
print(greeting)

# format引数２つ
print("{}{}".format(greeting,yeah))

# format,fstringの書き換え
balance = 100
print("balance: {}円".format(balance))
print(f"balance: {balance}円")

# type,idの表示
print(type("hello"))
print(type(1))
print(id(1))
