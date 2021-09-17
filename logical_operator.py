print("このアトラクションには制限があります。身長と年齢を教えてください。")
height = int(input("身長は？"))
age = int(input("年齢は？"))
min_height = 110
min_age = 10

if age >= min_age and height >= min_height:
    print(f"年齢は{age}歳、身長は{height}cmですね")
    print("どうぞお乗りください")
else:
    print(f"年齢は{age}歳、身長は{height}cmですね")
    print("もう少し大きくなってからまた来てくださいね")