print("このアトラクションには制限があります。身長と年齢を教えてください。")
height = int(input("身長"))
age = int(input("年齢"))
min_height = 110
min_age = 10

if age >= min_age and height >= min_height:
    print("どうぞお乗りください")
    print(f"年齢は{age}歳、身長は{height}cmです")
else:
    print(f"年齢は{age}歳、身長は{height}cmです")
    print(f"年齢は{min_age - age}歳、身長は{min_height - height}cm足りていません")